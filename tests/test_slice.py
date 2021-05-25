from src.slice.slice import sample_binom, slice_calculation

precision = 0.80
recall = 0.85
frequency = 0.30
interval_width = 0.05
alpha = 0.05
int_freq = 'True'


def test_sample_binom_returns_int():
    n = sample_binom()
    assert type(n) == int


def test_slice_calculation_returns_int():
    sum_pos_neg, total_pos, total_neg, true_pos, false_pos, true_neg, false_neg = \
        slice_calculation(precision=precision,
                          recall=recall,
                          frequency=frequency,
                          interval_width=interval_width,
                          alpha=alpha,
                          int_freq=int_freq)
    assert type(sum_pos_neg) == int
    assert type(total_pos) == int
    assert type(total_neg) == int
    assert type(true_pos) == int
    assert type(false_pos) == int
    assert type(true_neg) == int
    assert type(false_neg) == int


def test_slice_calculation_returns_internal_expected():
    sum_pos_neg, total_pos, total_neg, true_pos, false_pos, true_neg, false_neg = \
        slice_calculation(precision=precision,
                          recall=recall,
                          frequency=frequency,
                          interval_width=interval_width,
                          alpha=alpha,
                          int_freq=int_freq)

    assert sum_pos_neg == 883
    assert total_pos == 265
    assert total_neg == 618
    assert true_pos == 212
    assert false_pos == 53
    assert true_neg == 581
    assert false_neg == 37


def test_slice_calculation_returns_external_expected():
    sum_pos_neg, total_pos, total_neg, true_pos, false_pos, true_neg, false_neg = \
        slice_calculation(precision=precision,
                          recall=recall,
                          frequency=frequency,
                          interval_width=interval_width,
                          alpha=alpha,
                          int_freq='False')

    assert sum_pos_neg == 831
    assert total_pos == 265
    assert total_neg == 566
    assert true_pos == 212
    assert false_pos == 53
    assert true_neg == 529
    assert false_neg == 37
