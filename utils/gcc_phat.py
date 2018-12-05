"""
 Estimate time delay using GCC-PHAT 
 Copyright (c) 2017 Yihui Xiong

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import numpy as np
import matplotlib.pyplot as plt
from utils import wav, stft

def gcc_phat(sig, refsig, fs=1, max_tau=None, interp=16, plot=False, plot_title = 'GCC-PHAT'):
    '''
    This function computes the offset between the signal sig and the reference signal refsig
    using the Generalized Cross Correlation - Phase Transform (GCC-PHAT) method.
    '''
    
    eps = 1e-6
    # make sure the length for the FFT is larger or equal than len(sig) + len(refsig)
    n = sig.shape[0] + refsig.shape[0]

    # Generalized Cross Correlation Phase Transform
    SIG    = np.fft.fft(sig, n=n)
    REFSIG = np.fft.fft(refsig, n=n)

    S1 = stft.stft(sig,1024,512)
    S2 = stft.stft(refsig,1024,512)

    plt.subplot(121)
    plt.imshow(np.log(np.abs(S1)))
    plt.subplot(122)
    plt.imshow(np.log(np.abs(S2)))
    plt.show()

    R = SIG * np.conj(REFSIG)
    denom = np.abs(R)

    cc = np.fft.ifft(R / denom, n=(interp * n))

    max_shift = int(interp * n / 2)
    if max_tau:
        max_shift = np.minimum(int(interp * fs * max_tau), max_shift)

    cc = np.concatenate((cc[-max_shift:], cc[:max_shift+1]))

    # find max cross correlation index
    shift = np.argmax(np.abs(cc)) - max_shift
    tau = shift / float(interp * fs)
    
    if plot:
        t = np.arange(len(sig))/fs
        plt.subplot(311)
        plt.plot(t, sig)
        plt.subplot(312)
        plt.plot(t, refsig)
        plt.subplot(313)
        t = np.linspace(-max_shift, + max_shift+1, len(cc))/fs
        plt.plot(t, np.abs(cc))
        plt.scatter(shift,cc[shift+max_shift])
        plt.title(plot_title)
        plt.show()

    return tau, cc


def main():
    
    refsig = np.linspace(1, 10, 10)

    for i in range(0, 10):
        sig = np.concatenate((np.linspace(0, 0, i), refsig, np.linspace(0, 0, 10 - i)))
        offset, _ = gcc_phat(sig, refsig)
        print(offset)


if __name__ == "__main__":
    main()