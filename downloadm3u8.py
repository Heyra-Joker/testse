import m3u8

url = 'https://hj2404cca5.top/api/address/cf1d2f2efe35db1ca3f1e17bb0340be7?t=7608pcQSi4CbwHkftwvaookeg_6V6BZh5V7qLSd_7AJYCKw2_bVgECdjbm42h7PkEXB9aHv2-N6LgElLncfo0Hlan_a2zS51yg59UW6Fw-WWSt9E2uRHPpGkGbhodGf4QYcluiPiInqSPMCIvO5XqbH8ltPpzeXD1S8UnizMQC9Ek6cEO1BHzJPzWohRvgJTwcFhkrp4b3jeebqQ1zhWHJ90Ri5oMaQ7hhCZuCSdcyEok3gUxIwhc_BCH6yMZ7oD13eLyaDHysFfufIjlBpwAg425MRBPNdfiXioUoMEM1eUgcTE0h72nYmoiQdT-q_e'
playlist = m3u8.load(url)  # this could also be an absolute filename
print(playlist.segments)
print(playlist.target_duration)

res = playlist.dumps()
print(res)

# if you already have the content as string, use

# playlist = m3u8.loads('#EXTM3U8 ... etc ... ')