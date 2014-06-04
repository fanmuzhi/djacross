# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class Baseline(models.Model):
    baseline_id = models.BigIntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    baseline = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'baseline'

class Button(models.Model):
    button_id = models.IntegerField(primary_key=True)
    button_name = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'button'

class Chip(models.Model):
    chip_id = models.IntegerField(primary_key=True)
    part_number = models.ForeignKey('PartNumber')
    family = models.ForeignKey('PartNumber')
    chipid = models.CharField(db_column='chipID', max_length=20, blank=True) # Field name made lowercase.
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'chip'

class ConfigFile(models.Model):
    config_file_id = models.IntegerField(primary_key=True)
    part_number_part_number = models.ForeignKey('PartNumber')
    part_number_family = models.ForeignKey('PartNumber')
    software_version = models.CharField(max_length=60, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'config_file'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class Dut(models.Model):
    dut_id = models.IntegerField()
    part_number = models.ForeignKey('PartNumber')
    family = models.ForeignKey('PartNumber')
    serial_number = models.CharField(unique=True, max_length=30, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dut'

class ElapsedTime(models.Model):
    elapsed_time_id = models.IntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    elapsed_time = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'elapsed_time'

class ErrorInfo(models.Model):
    error_info_id = models.IntegerField(primary_key=True)
    error_code = models.IntegerField(blank=True, null=True)
    error_message = models.CharField(max_length=50, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'error_info'

class ExcutionMode(models.Model):
    excution_mode_id = models.IntegerField(primary_key=True)
    excution_mode = models.CharField(max_length=15, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'excution_mode'

class Family(models.Model):
    family_id = models.IntegerField(primary_key=True)
    family_name = models.CharField(max_length=10, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'family'

class FirmwareRevision(models.Model):
    firmware_revision_id = models.IntegerField(primary_key=True)
    part_number_part_number = models.ForeignKey('PartNumber')
    part_number_family = models.ForeignKey('PartNumber')
    firmware_revision = models.CharField(max_length=15, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'firmware_revision'

class FirmwareVersion(models.Model):
    firmware_version_id = models.IntegerField(primary_key=True)
    part_number = models.ForeignKey('PartNumber')
    family = models.ForeignKey('PartNumber')
    firmware_version = models.CharField(max_length=15, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'firmware_version'

class GlobalIdac(models.Model):
    global_idac_id = models.BigIntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    global_idac = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'global_idac'

class IcomCurrent(models.Model):
    icom_current_id = models.IntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    icom_current = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'icom_current'

class IdacGain(models.Model):
    idac_gain_id = models.BigIntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    idac_gain = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'idac_gain'

class IddDeepSleep(models.Model):
    idd_deep_sleep_id = models.IntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    idd_deep_sleep = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'idd_deep_sleep'

class IddSleep1(models.Model):
    idd_sleep1_id = models.IntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    update_time = models.DateTimeField(blank=True, null=True)
    idd_sleep1 = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'idd_sleep1'

class IddValue(models.Model):
    idd_value_id = models.IntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    idd_value = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'idd_value'

class LocalIdac(models.Model):
    local_idac_id = models.BigIntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    local_idac = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'local_idac'

class Noise(models.Model):
    noise_id = models.BigIntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    noise = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'noise'

class Operator(models.Model):
    operator_id = models.IntegerField(primary_key=True)
    operator = models.CharField(max_length=10, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'operator'

class PartNumber(models.Model):
    part_number_id = models.IntegerField()
    family = models.ForeignKey(Family)
    part_number = models.CharField(max_length=20, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'part_number'

class RawCountAverage(models.Model):
    raw_count_average_id = models.BigIntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    raw_count_average = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'raw_count_average'

class RawCountNoise(models.Model):
    raw_count_noise_id = models.BigIntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    raw_count_noise = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'raw_count_noise'

class Rawdata(models.Model):
    rawdata_id = models.BigIntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    rawdata = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'rawdata'

class SelfcapBaseline(models.Model):
    selfcap_baseline_id = models.BigIntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    selfcap_baseline = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'selfcap_baseline'

class SelfcapNoise(models.Model):
    selfcap_noise_id = models.IntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    selfcap_noise = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'selfcap_noise'

class SelfcapRawdata(models.Model):
    selfcap_rawdata_id = models.BigIntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    selfcap_rawdata = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'selfcap_rawdata'

class SelfcapSignal(models.Model):
    selfcap_signal_id = models.BigIntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    selfcap_signal = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'selfcap_signal'

class SensorScale(models.Model):
    sensor_scale_id = models.IntegerField(primary_key=True)
    part_number = models.ForeignKey(PartNumber)
    family = models.ForeignKey(PartNumber)
    sensor_rows = models.IntegerField(blank=True, null=True)
    sensor_columns = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sensor_scale'

class Signal(models.Model):
    signal_id = models.BigIntegerField(primary_key=True)
    test = models.ForeignKey('Test')
    signal = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'signal'

class SoftwareVersion(models.Model):
    software_version_id = models.IntegerField(primary_key=True)
    part_number = models.ForeignKey(PartNumber)
    family = models.ForeignKey(PartNumber)
    software_version = models.CharField(max_length=15, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'software_version'

class Test(models.Model):
    test_id = models.IntegerField(unique=True)
    dut = models.ForeignKey(Dut)
    part_number = models.ForeignKey(Dut)
    family = models.ForeignKey(Dut)
    test_station = models.ForeignKey('TestStation')
    firmware_revision = models.ForeignKey(FirmwareRevision)
    operator = models.ForeignKey(Operator)
    test_result = models.ForeignKey('TestResult')
    firmware_version = models.ForeignKey(FirmwareVersion)
    excution_mode = models.ForeignKey(ExcutionMode)
    error_info = models.ForeignKey(ErrorInfo)
    software_version = models.ForeignKey(SoftwareVersion)
    test_facility = models.ForeignKey('TestFacility')
    config_file = models.ForeignKey(ConfigFile)
    test_status = models.ForeignKey('TestStatus')
    button = models.ForeignKey(Button)
    chip = models.ForeignKey(Chip)
    sensor_scale = models.ForeignKey(SensorScale)
    test_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'test'

class TestFacility(models.Model):
    test_facility_id = models.IntegerField(primary_key=True)
    test_facility_name = models.CharField(max_length=15, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'test_facility'

class TestResult(models.Model):
    test_result_id = models.IntegerField(primary_key=True)
    test_result = models.CharField(max_length=10, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'test_result'

class TestStation(models.Model):
    test_station_id = models.IntegerField(primary_key=True)
    test_station = models.CharField(max_length=10, blank=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'test_station'

class TestStatus(models.Model):
    test_status_id = models.IntegerField(primary_key=True)
    test_status = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'test_status'

class VcomVoltage(models.Model):
    vcom_voltage_id = models.IntegerField(primary_key=True)
    test = models.ForeignKey(Test)
    vcom_voltage = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vcom_voltage'

