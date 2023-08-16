This repo contains various scenarios to test moving model between apps.
##### 1. basic
     "test_one",
     "test_two",

##### 2. moving model with m2m field with through model
     "test_four",
     "test_five",

##### 3. moving model with m2m field with through model and adding fk and m2m field to other 2 models in old app
     "test_six",
     "test_seven",

##### 4. moving model with inherited abstract model
     "test_eight",
     "test_nine",

##### 5. moving model with Generic foreign key
     "test_ten",
     "test_eleven",

##### 6. moving model + adding field simultaneously
     "test_twelve",
     "test_thirteen",

##### 7. one model is moved and another model is renamed simultaneously.
     "test_fourteen",
     "test_fifteen",
     "test_sixteen",

##### 8. two models are simultaneously moved - one managed and one unmanaged
     "test_seventeen",
     "test_eighteen",

##### 9. moving model with inherited non abstract model
     "test_nineteen",
     "test_twenty",

##### 10. moving model by just changing app_label in Model's meta
     "test_twentyone",
     "test_twentytwo",

#### moving two models at once - both managed
     "app_a",
     "app_b",

note: moving multiple models at once is possible only when 