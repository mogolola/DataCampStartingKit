# RAMP starting kit on American Crop Yield Prediction

Authors: Mo YANG, Shuopeng WANG, Zizhao LI & Qixiang PENG



Agricultural monitoring, in particular in developing countries, can help prevent famine and support humanitarian efforts. A central challenge of this is yield estimation, which is to predict crop yields before harvesting. 
 
These multi-spectral remote sensing images contain a wealth of information on vegetation growth and on agricultural outcomes which could be used for crop yields prediction. Also, they are globally available and economical data source. 
 
The challenge is to design an algorithm to automatically predict crop yield based on remote sensing data.


#### Set up

Open a terminal and

1. install the `ramp-workflow` library (if not already done)
  ```
  $ pip install git+https://github.com/paris-saclay-cds/ramp-workflow.git
  ```
  
2. Follow the ramp-kits instructions from the [wiki](https://github.com/paris-saclay-cds/ramp-workflow/wiki/Getting-started-with-a-ramp-kit)

#### Local notebook

Get started on this RAMP with the [dedicated notebook](starting_kit.ipynb).

#### Test

to test the starting kit submission (`submissions/starting_kit`)

```
ramp_test_submission --submission=starting_kit
```

#### Help
Go to the `ramp-workflow` [wiki](https://github.com/paris-saclay-cds/ramp-workflow/wiki) for more help on the [RAMP](http:www.ramp.studio) ecosystem.
