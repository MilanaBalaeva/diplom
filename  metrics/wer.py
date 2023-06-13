import jiwer


def calculate_per(reference, hypothesis):
    hyp = hypothesis.read()
    ref = reference.read()
    wer = jiwer.wer(ref, hyp)
    return wer