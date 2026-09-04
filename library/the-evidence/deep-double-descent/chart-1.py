# Model-wise double descent: ResNet18 on CIFAR-10 with 15% label noise.
#
# Provenance. The series below is computed from the authors' released raw data
# (Nakkiran et al. 2019), bucket gs://hml-public/dd/cifar10-resnet18k-p15-adam-reps
# reachable at https://storage.googleapis.com/hml-public/dd/cifar10-resnet18k-p15-adam-reps
# and indexed from https://gitlab.com/harvard-machine-learning/double-descent.
# Each ResNet18 is parameterized by a width k (standard ResNet18 is k=64); the
# bucket holds five training runs. For each width the final-epoch error is taken,
# averaged over the five runs. Test error is measured on clean labels and then
# remapped to the noisy test distribution with the paper's own transform,
# test_noisy = 1 - (1-p)(1-test_clean) + test_clean * p/9, p = 0.15, exactly as
# in the authors' intro_resnet_plot.ipynb. Train error is on the noisy training
# labels. Values are rounded to four decimals.

import plotly.graph_objects as go

width = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
         39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
         57, 58, 59, 60, 61, 62, 63, 64]

test_error = [0.5351, 0.395, 0.3517, 0.3397, 0.3476, 0.3697, 0.3882, 0.4085,
              0.4095, 0.4127, 0.4084, 0.3966, 0.3934, 0.3855, 0.3807, 0.3675,
              0.3676, 0.3585, 0.3575, 0.3549, 0.3471, 0.3428, 0.3428, 0.3421,
              0.3338, 0.3308, 0.3318, 0.331, 0.3278, 0.3274, 0.3258, 0.3244,
              0.3178, 0.3153, 0.3171, 0.3152, 0.3115, 0.3113, 0.3114, 0.3116,
              0.3089, 0.3098, 0.3062, 0.3029, 0.3048, 0.3033, 0.3, 0.3021,
              0.3014, 0.2985, 0.2981, 0.2948, 0.2994, 0.294, 0.296, 0.2944,
              0.2982, 0.2944, 0.2942, 0.2929, 0.2932, 0.2924, 0.291, 0.2911]

train_error = [0.534, 0.3825, 0.3184, 0.2809, 0.258, 0.2318, 0.1988, 0.1628,
               0.1205, 0.0831, 0.0514, 0.0317, 0.0187, 0.0127, 0.0098, 0.0069,
               0.0048, 0.0042, 0.0037, 0.003, 0.0024, 0.0021, 0.002, 0.0019,
               0.0016, 0.0012, 0.001, 0.0012, 0.0012, 0.0011, 0.0009, 0.0008,
               0.0007, 0.001, 0.0008, 0.0009, 0.0008, 0.0008, 0.0005, 0.0008,
               0.0007, 0.0006, 0.0006, 0.0005, 0.0007, 0.0006, 0.0005, 0.0006,
               0.0004, 0.0004, 0.0004, 0.0005, 0.0006, 0.0004, 0.0005, 0.0004,
               0.0005, 0.0005, 0.0003, 0.0006, 0.0005, 0.0004, 0.0005, 0.0004]

fig = go.Figure()
fig.add_trace(go.Scatter(name="Test error", x=width, y=test_error, mode="lines"))
fig.add_trace(go.Scatter(name="Train error", x=width, y=train_error, mode="lines"))
fig.update_layout(
    xaxis_title="ResNet18 width parameter k  (standard ResNet18 is k = 64)",
    yaxis_title="Error on CIFAR-10 with 15% label noise",
)
fig.update_yaxes(rangemode="tozero")
