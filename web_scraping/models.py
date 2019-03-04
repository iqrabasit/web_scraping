from django.db import models


class TblConsultancyData(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    procurement_title = models.TextField(blank=True, null=True)
    procurement_name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    publish_date = models.TextField(blank=True, null=True)
    close_date = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    tender_notice = models.TextField(blank=True, null=True)
    bidding_document = models.TextField(blank=True, null=True)
    page_no = models.IntegerField()
    row_id = models.TextField(blank=True, null=True)
