from django.db import models

# moved from test_six to test_seven
class MyModel(models.Model):
    main_fk = models.ForeignKey('test_six.MainModel', on_delete=models.CASCADE)
    m2m_fk = models.ForeignKey('test_six.MyModelM2M', on_delete=models.CASCADE)

    class Meta:
        db_table="test_six_mymodel"
