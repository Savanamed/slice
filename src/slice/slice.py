from statsmodels.stats import proportion
from argparse import ArgumentParser
from columnar import columnar


def sample_binom(p_0=0.05, interval=0.05, n_start=1, n_max=10 ** 6, alpha=0.05):
    """

    :param p_0:
    :param interval:
    :param n_start:
    :param n_max:
    :param alpha:
    :return:
        n =
    """
    stop = False

    n = max(0, round(n_start - 1))

    while (stop == False) & (n < n_max):
        n = n + 1
        x = round(n * p_0)
        confidence_interval = proportion.proportion_confint(x, n, method="beta", alpha=alpha)
        width = confidence_interval[1] - confidence_interval[0]
        stop = width < 2 * interval
    return n


def slice_calculation(precision, recall, frequency, interval_width, alpha, int_freq):
    """

    :param precision: float
    :param recall: float
    :param frequency: float
    :param interval_width: float
    :param alpha: float
    :param int_freq: bool
    :return:
        total_positive: Classified as belonging to a class
        total_negative: Classified as not belonging to a class
        total: Sum of total_positive and total_negative
        true_positive: Correctly classified as belonging to your class
        true_negative: Correctly classified as not belonging to your class
        false_positive: Incorrectly classified as belonging to your class
        false_negative: Incorrectly classified as not belonging to your class
    """

    n_precision = sample_binom(p_0=precision, interval=interval_width, alpha=alpha)
    n_recall = sample_binom(p_0=recall, interval=interval_width, alpha=alpha)
    # True positives
    tp_precision = n_precision * precision
    tp_recall = n_recall * recall
    # False positives
    fp_precision = n_precision - tp_precision
    fp_recall = tp_recall / (precision / (1 - precision))
    # False negatives
    fn_precision = tp_precision / (recall / (1 - recall))
    fn_recall = n_recall - tp_recall

    # True negatives
    val_tn_precision_external = (
                                        (tp_precision + fn_precision) * (
                                            1 - frequency) - frequency * fp_precision
                                ) / frequency

    tn_precision_external = max(0, val_tn_precision_external)

    val_tn_precision_internal = (
                                        (tp_precision + fp_precision) * (
                                            1 - frequency) - frequency * fn_precision
                                ) / frequency

    tn_precision_internal = max(0, val_tn_precision_internal)

    val_tn_recall_external = (
                                     (tp_recall + fn_recall) * (1 - frequency) - frequency * fp_recall
                             ) / frequency

    tn_recall_external = max(0, val_tn_recall_external)

    val_tn_recall_internal = (
                                     (tp_recall + fp_recall) * (1 - frequency) - frequency * fn_recall
                             ) / frequency

    tn_recall_internal = max(0, val_tn_recall_internal)

    if int_freq:
        tn_precision = tn_precision_internal
        tn_recall = tn_recall_internal
    else:
        tn_precision = tn_precision_external
        tn_recall = tn_recall_external

    true_pos = round(max(tp_precision, tp_recall))
    false_pos = round(max(fp_precision, fp_recall))
    true_neg = round(max(tn_precision, tn_recall))
    false_neg = round(max(fn_precision, fn_recall))

    # Total positives

    total_pos = true_pos + false_pos

    # Total negatives

    total_neg = false_neg + true_neg

    # Total

    sum_pos_neg = total_pos + total_neg

    return (
        sum_pos_neg,
        total_pos,
        total_neg,
        true_pos,
        false_pos,
        true_neg,
        false_neg,
        )


if __name__ == "__main__":
    parser = ArgumentParser(description="Input parameters for SLiCE")
    parser.add_argument("--precision", type=float, default=0.80, required=False, dest="precision")
    parser.add_argument("--recall", type=float, default=0.85, required=False, dest="recall")
    parser.add_argument(
        "--frequency", type=float, default=0.3, required=False, dest="frequency"
        )
    parser.add_argument("--alpha", type=float, default=0.05, required=False, dest="alpha")
    parser.add_argument("--interval-width", type=float, default=0.05, required=False, dest="interval_width")
    parser.add_argument("--int_freq", type=bool, default=True, required=False, dest="int_freq")

    args = parser.parse_args()

    argument_headers = [
        "--precision",
        "--recall",
        "--frequency",
        "--alpha",
        "--interval-width",
        "--int_freq",
        ]

    arguments = [
        [
            args.precision,
            args.recall,
            args.frequency,
            args.alpha,
            args.interval_width,
            args.int_freq,
            ]
        ]

    configuration = columnar(arguments, argument_headers, no_borders=False)
    print("Selected parameter values:")
    print(configuration)

    (
        total,
        total_positive,
        total_negative,
        true_positive,
        false_positive,
        true_negative,
        false_negative,
        ) = slice_calculation(
        precision=args.precision,
        recall=args.recall,
        frequency=args.frequency,
        interval_width=args.interval_width,
        alpha=args.alpha,
        int_freq=args.int_freq,
        )

    headers = ["Total", "Total positive", "Total negative", "TP", "FP", "TN", "FN"]

    data = [
        [
            total,
            total_positive,
            total_negative,
            true_positive,
            false_positive,
            true_negative,
            false_negative,
            ]
        ]

    table = columnar(data, headers, no_borders=False)
    print("The results of SLiCE based on the selected parameter values:")
    print(table)
