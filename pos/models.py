# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BatchJobLog(models.Model):
    job_id = models.CharField(db_column='JOB_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    job_date = models.CharField(db_column='JOB_DATE', max_length=10)  # Field name made lowercase.
    seq_no = models.IntegerField(db_column='SEQ_NO')  # Field name made lowercase.
    target_table_name = models.CharField(db_column='TARGET_TABLE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    std_start_date = models.CharField(db_column='STD_START_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    std_end_date = models.CharField(db_column='STD_END_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    job_status_cd = models.CharField(db_column='JOB_STATUS_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    job_row_count = models.IntegerField(db_column='JOB_ROW_COUNT', blank=True, null=True)  # Field name made lowercase.
    job_start_date = models.CharField(db_column='JOB_START_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    job_end_date = models.CharField(db_column='JOB_END_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BATCH_JOB_LOG'
        unique_together = (('job_id', 'job_date', 'seq_no'),)


class JunohrTodo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'JUNOHR_todo'


class MigTjsCustTicket(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    start_dt = models.CharField(db_column='START_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    end_dt = models.CharField(db_column='END_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    org_cnt = models.DecimalField(db_column='ORG_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    use_cnt = models.DecimalField(db_column='USE_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    res_cnt = models.DecimalField(db_column='RES_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MIG_TJS_CUST_TICKET'


class SmsMigTarget(models.Model):
    reg_no = models.AutoField(db_column='REG_NO', primary_key=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    contents = models.CharField(db_column='CONTENTS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    etc = models.CharField(db_column='ETC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMS_MIG_TARGET'


class SysSpLog(models.Model):
    line_no = models.AutoField(db_column='LINE_NO', primary_key=True)  # Field name made lowercase.
    object_nm = models.CharField(db_column='OBJECT_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    type_cd = models.CharField(db_column='TYPE_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sqlcmd = models.TextField(db_column='SQLCMD', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_tm = models.DateTimeField(db_column='UPD_TM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SYS_SP_LOG'


class TicTmp(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    res_cnt = models.DecimalField(db_column='RES_CNT', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIC_TMP'


class TjeEtlHis(models.Model):
    etl_dt = models.CharField(db_column='ETL_DT', primary_key=True, max_length=8)  # Field name made lowercase.
    etl_cd = models.CharField(db_column='ETL_CD', max_length=40)  # Field name made lowercase.
    etl_ord = models.DecimalField(db_column='ETL_ORD', max_digits=18, decimal_places=0)  # Field name made lowercase.
    etl_start_dtm = models.DateTimeField(db_column='ETL_START_DTM', blank=True, null=True)  # Field name made lowercase.
    etl_end_dtm = models.DateTimeField(db_column='ETL_END_DTM', blank=True, null=True)  # Field name made lowercase.
    etl_rslt_cd = models.CharField(db_column='ETL_RSLT_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etl_rslt_con = models.CharField(db_column='ETL_RSLT_CON', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJE_ETL_HIS'
        unique_together = (('etl_dt', 'etl_cd', 'etl_ord'),)


class TjeEtlMst(models.Model):
    etl_cd = models.CharField(db_column='ETL_CD', primary_key=True, max_length=40)  # Field name made lowercase.
    etl_div_cd = models.CharField(db_column='ETL_DIV_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etl_nm = models.CharField(db_column='ETL_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    etl_kor_nm = models.CharField(db_column='ETL_KOR_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    etl_prog_type = models.CharField(db_column='ETL_PROG_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etl_prog_seq = models.DecimalField(db_column='ETL_PROG_SEQ', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    etl_prog_cycle = models.CharField(db_column='ETL_PROG_CYCLE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etl_prog_nm = models.CharField(db_column='ETL_PROG_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    etl_desc = models.CharField(db_column='ETL_DESC', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    etl_prog_start_time = models.CharField(db_column='ETL_PROG_START_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJE_ETL_MST'


class TjsAcsTknMng(models.Model):
    token_id = models.CharField(db_column='TOKEN_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    sys_div_cd = models.CharField(db_column='SYS_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(db_column='TOKEN', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    prvd_agnc_cd = models.CharField(db_column='PRVD_AGNC_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ACS_TKN_MNG'


class TjsApiCfg(models.Model):
    api_cd = models.CharField(db_column='API_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    api_tp = models.CharField(db_column='API_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    api_adr = models.CharField(db_column='API_ADR', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_API_CFG'


class TjsCalendar(models.Model):
    date = models.CharField(max_length=8, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    month = models.CharField(max_length=2, blank=True, null=True)
    day = models.CharField(max_length=2, blank=True, null=True)
    week = models.CharField(max_length=1, blank=True, null=True)
    cnt = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TJS_CALENDAR'


class TjsCalendarMas(models.Model):
    date_cd = models.CharField(db_column='DATE_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date_nm = models.CharField(db_column='DATE_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_dt = models.CharField(db_column='DATE_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    hldy_yn = models.CharField(db_column='HLDY_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CALENDAR_MAS'


class TjsCatid(models.Model):
    biz_no = models.CharField(db_column='BIZ_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    shop_nm = models.CharField(db_column='SHOP_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    catid_main = models.CharField(db_column='CATID_MAIN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    catid_gift = models.CharField(db_column='CATID_GIFT', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CATID'


class TjsConfig(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    module_cd = models.CharField(db_column='MODULE_CD', max_length=10)  # Field name made lowercase.
    ctrl_cd = models.CharField(db_column='CTRL_CD', max_length=10)  # Field name made lowercase.
    ctrl_nm = models.CharField(db_column='CTRL_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ctrl_vl = models.CharField(db_column='CTRL_VL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ctrl_dc = models.CharField(db_column='CTRL_DC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ctrl_tp = models.CharField(db_column='CTRL_TP', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ref_cd = models.CharField(db_column='REF_CD', max_length=6, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CONFIG'
        unique_together = (('shop_cd', 'module_cd', 'ctrl_cd'),)


class TjsConfigTmp(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    module_cd = models.CharField(db_column='MODULE_CD', max_length=10)  # Field name made lowercase.
    ctrl_cd = models.CharField(db_column='CTRL_CD', max_length=10)  # Field name made lowercase.
    ctrl_nm = models.CharField(db_column='CTRL_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ctrl_vl = models.CharField(db_column='CTRL_VL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ctrl_dc = models.CharField(db_column='CTRL_DC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ctrl_tp = models.CharField(db_column='CTRL_TP', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ref_cd = models.CharField(db_column='REF_CD', max_length=6, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CONFIG_TMP'


class TjsCtnsForm(models.Model):
    ctns_frm_id = models.CharField(db_column='CTNS_FRM_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    contents = models.CharField(db_column='CONTENTS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ctns_kd_cd = models.CharField(db_column='CTNS_KD_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ctns_sndr_id = models.CharField(db_column='CTNS_SNDR_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ad_yn = models.CharField(db_column='AD_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    term_yn = models.CharField(db_column='TERM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    indv_nm_yn = models.CharField(db_column='INDV_NM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CTNS_FORM'


class TjsCtnsMasSndReq(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    ctns_snd_no = models.CharField(db_column='CTNS_SND_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ctns_snd_dt = models.CharField(db_column='CTNS_SND_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ctns_snd_req_id = models.CharField(db_column='CTNS_SND_REQ_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ctns_snd_mdia_cd = models.CharField(db_column='CTNS_SND_MDIA_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ctns_kd_cd = models.CharField(db_column='CTNS_KD_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    contents = models.CharField(db_column='CONTENTS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcpt_tel_no = models.CharField(db_column='RCPT_TEL_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    req_stat_cd = models.CharField(db_column='REQ_STAT_CD', max_length=3)  # Field name made lowercase.
    ad_yn = models.CharField(db_column='AD_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    term_yn = models.CharField(db_column='TERM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    indv_nm_yn = models.CharField(db_column='INDV_NM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CTNS_MAS_SND_REQ'


class TjsCtnsRsrvList(models.Model):
    ctns_rsrv_id = models.CharField(db_column='CTNS_RSRV_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rsrv_stat_cd = models.CharField(db_column='RSRV_STAT_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    snd_dt = models.CharField(db_column='SND_DT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    snd_hr = models.CharField(db_column='SND_HR', max_length=4, blank=True, null=True)  # Field name made lowercase.
    snd_mnt = models.CharField(db_column='SND_MNT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    contents = models.CharField(db_column='CONTENTS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ctns_kd_cd = models.CharField(db_column='CTNS_KD_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ctns_snd_mdia_cd = models.CharField(db_column='CTNS_SND_MDIA_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ad_yn = models.CharField(db_column='AD_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    term_yn = models.CharField(db_column='TERM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    indv_nm_yn = models.CharField(db_column='INDV_NM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    period = models.CharField(db_column='PERIOD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    period_dtl = models.CharField(db_column='PERIOD_DTL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cron_expr = models.CharField(db_column='CRON_EXPR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ctns_frm_id = models.CharField(db_column='CTNS_FRM_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ctns_rsrv_nm = models.CharField(db_column='CTNS_RSRV_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CTNS_RSRV_LIST'


class TjsCtnsSnd(models.Model):
    ctns_snd_id = models.CharField(db_column='CTNS_SND_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    ctns_snd_req_id = models.CharField(db_column='CTNS_SND_REQ_ID', max_length=20)  # Field name made lowercase.
    ctns_snd_sno = models.IntegerField(db_column='CTNS_SND_SNO', blank=True, null=True)  # Field name made lowercase.
    ctns_kd_cd = models.CharField(db_column='CTNS_KD_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ctns_snd_mdia_cd = models.CharField(db_column='CTNS_SND_MDIA_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ctns_frm_id = models.CharField(db_column='CTNS_FRM_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcpt_tel_no = models.CharField(db_column='RCPT_TEL_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cust_div_cd = models.CharField(db_column='CUST_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    snd_pcs_stat_cd = models.CharField(db_column='SND_PCS_STAT_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    rsl_rci_dtm = models.DateTimeField(db_column='RSL_RCI_DTM', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    contents = models.CharField(db_column='CONTENTS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ctns_img_con = models.CharField(db_column='CTNS_IMG_CON', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    snd_anrm_pcs_rsn_cd = models.CharField(db_column='SND_ANRM_PCS_RSN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fail_rsn_con = models.CharField(db_column='FAIL_RSN_CON', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    snd_req_dtm = models.DateTimeField(db_column='SND_REQ_DTM', blank=True, null=True)  # Field name made lowercase.
    snd_reqpe_id = models.CharField(db_column='SND_REQPE_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    snd_req_shop_cd = models.CharField(db_column='SND_REQ_SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcpt_seq = models.IntegerField(db_column='RCPT_SEQ', blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CTNS_SND'


class TjsCtnsSndCls(models.Model):
    clos_dt = models.CharField(db_column='CLOS_DT', primary_key=True, max_length=8)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    snd_div_cd = models.CharField(db_column='SND_DIV_CD', max_length=2)  # Field name made lowercase.
    snd_cnt = models.IntegerField(db_column='SND_CNT', blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='PRICE', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CTNS_SND_CLS'
        unique_together = (('clos_dt', 'shop_cd', 'snd_div_cd'),)


class TjsCtnsSndGrp(models.Model):
    ctns_snd_grp_id = models.CharField(db_column='CTNS_SND_GRP_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ctns_sndr_id = models.CharField(db_column='CTNS_SNDR_ID', max_length=200)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CTNS_SND_GRP'
        unique_together = (('ctns_snd_grp_id', 'line_no'),)


class TjsCtnsSndInfMng(models.Model):
    ctns_sndr_id = models.CharField(db_column='CTNS_SNDR_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    ctns_snd_key = models.CharField(db_column='CTNS_SND_KEY', max_length=40)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    snd_div_cd = models.CharField(db_column='SND_DIV_CD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CTNS_SND_INF_MNG'
        unique_together = (('ctns_sndr_id', 'ctns_snd_key'),)


class TjsCtnsSndReq(models.Model):
    ctns_snd_req_id = models.CharField(db_column='CTNS_SND_REQ_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    ctns_snd_mdia_cd = models.CharField(db_column='CTNS_SND_MDIA_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ctns_kd_cd = models.CharField(db_column='CTNS_KD_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    snd_req_dtm = models.CharField(db_column='SND_REQ_DTM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    onln_bat_div_cd = models.CharField(db_column='ONLN_BAT_DIV_CD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    snd_tp_cd = models.CharField(db_column='SND_TP_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    snd_tel_no = models.CharField(db_column='SND_TEL_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctns_rsrv_id = models.CharField(db_column='CTNS_RSRV_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    snd_rsrv_dtm = models.CharField(db_column='SND_RSRV_DTM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    snd_comp_dtm = models.CharField(db_column='SND_COMP_DTM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ctns_snd_stat_cd = models.CharField(db_column='CTNS_SND_STAT_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ad_yn = models.CharField(db_column='AD_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    term_yn = models.CharField(db_column='TERM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    indv_nm_yn = models.CharField(db_column='INDV_NM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ets_etp_nm = models.CharField(db_column='ETS_ETP_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    res_req_id = models.CharField(db_column='RES_REQ_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CTNS_SND_REQ'


class TjsCustDesigner(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    main_yn = models.CharField(db_column='MAIN_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_DESIGNER'
        unique_together = (('cust_cd', 'shop_cd', 'line_no'),)


class TjsCustDesigner20210516(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    main_yn = models.CharField(db_column='MAIN_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_DESIGNER_20210516'


class TjsCustFamily(models.Model):
    fam_cd = models.CharField(db_column='FAM_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cp_tel = models.CharField(db_column='CP_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fam_tp = models.CharField(db_column='FAM_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    main_yn = models.CharField(db_column='MAIN_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_FAMILY'
        unique_together = (('fam_cd', 'line_no'),)


class TjsCustGrade(models.Model):
    lv_cd = models.CharField(db_column='LV_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    lv_nm = models.CharField(db_column='LV_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    st_pnt = models.DecimalField(db_column='ST_PNT', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ed_pnt = models.DecimalField(db_column='ED_PNT', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    st_visit_cnt = models.DecimalField(db_column='ST_VISIT_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ed_visit_cnt = models.DecimalField(db_column='ED_VISIT_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_GRADE'


class TjsCustInfo(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_card_no = models.CharField(db_column='CUST_CARD_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender_cd = models.CharField(db_column='GENDER_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lv_cd = models.CharField(db_column='LV_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birth_dt = models.CharField(db_column='BIRTH_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    birth_div = models.CharField(db_column='BIRTH_DIV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cp_tel = models.CharField(db_column='CP_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zip_cd = models.CharField(db_column='ZIP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    adr = models.CharField(db_column='ADR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    adr_dtl = models.CharField(db_column='ADR_DTL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    marry_yn = models.CharField(db_column='MARRY_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nation_cd = models.CharField(db_column='NATION_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vst_rt_cd = models.CharField(db_column='VST_RT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    frst_vst_dt = models.CharField(db_column='FRST_VST_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lst_vst_dt = models.CharField(db_column='LST_VST_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    anniv_dt = models.CharField(db_column='ANNIV_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sms_yn = models.CharField(db_column='SMS_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vst_cnt = models.DecimalField(db_column='VST_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcmd_cnt = models.DecimalField(db_column='RCMD_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    car_no = models.CharField(db_column='CAR_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    drink_inf = models.CharField(db_column='DRINK_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shmp_tch_inf = models.CharField(db_column='SHMP_TCH_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shmp_inf = models.CharField(db_column='SHMP_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tip_inf = models.CharField(db_column='TIP_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taste_1 = models.CharField(db_column='TASTE_1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taste_2 = models.CharField(db_column='TASTE_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fam_cd = models.CharField(db_column='FAM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    warn_yn = models.CharField(db_column='WARN_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    anniv_tp = models.CharField(db_column='ANNIV_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    birth_yy = models.CharField(db_column='BIRTH_YY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    birth_md = models.CharField(db_column='BIRTH_MD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    inactive_yn = models.CharField(db_column='INACTIVE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fnl_shop_cd = models.CharField(db_column='FNL_SHOP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_INFO'


class TjsCustInfo20210412(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_card_no = models.CharField(db_column='CUST_CARD_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender_cd = models.CharField(db_column='GENDER_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lv_cd = models.CharField(db_column='LV_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birth_dt = models.CharField(db_column='BIRTH_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    birth_div = models.CharField(db_column='BIRTH_DIV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cp_tel = models.CharField(db_column='CP_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zip_cd = models.CharField(db_column='ZIP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    adr = models.CharField(db_column='ADR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    adr_dtl = models.CharField(db_column='ADR_DTL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    marry_yn = models.CharField(db_column='MARRY_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nation_cd = models.CharField(db_column='NATION_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vst_rt_cd = models.CharField(db_column='VST_RT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    frst_vst_dt = models.CharField(db_column='FRST_VST_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lst_vst_dt = models.CharField(db_column='LST_VST_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    anniv_dt = models.CharField(db_column='ANNIV_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sms_yn = models.CharField(db_column='SMS_YN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vst_cnt = models.DecimalField(db_column='VST_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcmd_cnt = models.DecimalField(db_column='RCMD_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    car_no = models.CharField(db_column='CAR_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    drink_inf = models.CharField(db_column='DRINK_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shmp_tch_inf = models.CharField(db_column='SHMP_TCH_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shmp_inf = models.CharField(db_column='SHMP_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tip_inf = models.CharField(db_column='TIP_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taste_1 = models.CharField(db_column='TASTE_1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taste_2 = models.CharField(db_column='TASTE_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fam_cd = models.CharField(db_column='FAM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    warn_yn = models.CharField(db_column='WARN_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_INFO_20210412'


class TjsCustInfo20210516(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_card_no = models.CharField(db_column='CUST_CARD_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender_cd = models.CharField(db_column='GENDER_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lv_cd = models.CharField(db_column='LV_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birth_dt = models.CharField(db_column='BIRTH_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    birth_div = models.CharField(db_column='BIRTH_DIV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cp_tel = models.CharField(db_column='CP_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zip_cd = models.CharField(db_column='ZIP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    adr = models.CharField(db_column='ADR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    adr_dtl = models.CharField(db_column='ADR_DTL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    marry_yn = models.CharField(db_column='MARRY_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nation_cd = models.CharField(db_column='NATION_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vst_rt_cd = models.CharField(db_column='VST_RT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    frst_vst_dt = models.CharField(db_column='FRST_VST_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lst_vst_dt = models.CharField(db_column='LST_VST_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    anniv_dt = models.CharField(db_column='ANNIV_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sms_yn = models.CharField(db_column='SMS_YN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vst_cnt = models.DecimalField(db_column='VST_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcmd_cnt = models.DecimalField(db_column='RCMD_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    car_no = models.CharField(db_column='CAR_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    drink_inf = models.CharField(db_column='DRINK_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shmp_tch_inf = models.CharField(db_column='SHMP_TCH_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shmp_inf = models.CharField(db_column='SHMP_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tip_inf = models.CharField(db_column='TIP_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taste_1 = models.CharField(db_column='TASTE_1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taste_2 = models.CharField(db_column='TASTE_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fam_cd = models.CharField(db_column='FAM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    warn_yn = models.CharField(db_column='WARN_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    anniv_tp = models.CharField(db_column='ANNIV_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    birth_yy = models.CharField(db_column='BIRTH_YY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    birth_md = models.CharField(db_column='BIRTH_MD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    inactive_yn = models.CharField(db_column='INACTIVE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fnl_shop_cd = models.CharField(db_column='FNL_SHOP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_INFO_20210516'


class TjsCustInfoEx(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_card_no = models.CharField(db_column='CUST_CARD_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender_cd = models.CharField(db_column='GENDER_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lv_cd = models.CharField(db_column='LV_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birth_dt = models.CharField(db_column='BIRTH_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    birth_div = models.CharField(db_column='BIRTH_DIV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cp_tel = models.CharField(db_column='CP_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zip_cd = models.CharField(db_column='ZIP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    adr = models.CharField(db_column='ADR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    adr_dtl = models.CharField(db_column='ADR_DTL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    marry_yn = models.CharField(db_column='MARRY_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nation_cd = models.CharField(db_column='NATION_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vst_rt_cd = models.CharField(db_column='VST_RT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    frst_vst_dt = models.CharField(db_column='FRST_VST_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lst_vst_dt = models.CharField(db_column='LST_VST_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    anniv_dt = models.CharField(db_column='ANNIV_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sms_yn = models.CharField(db_column='SMS_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vst_cnt = models.DecimalField(db_column='VST_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcmd_cnt = models.DecimalField(db_column='RCMD_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    car_no = models.CharField(db_column='CAR_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    drink_inf = models.CharField(db_column='DRINK_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shmp_tch_inf = models.CharField(db_column='SHMP_TCH_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shmp_inf = models.CharField(db_column='SHMP_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tip_inf = models.CharField(db_column='TIP_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taste_1 = models.CharField(db_column='TASTE_1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taste_2 = models.CharField(db_column='TASTE_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fam_cd = models.CharField(db_column='FAM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    warn_yn = models.CharField(db_column='WARN_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    anniv_tp = models.CharField(db_column='ANNIV_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    birth_yy = models.CharField(db_column='BIRTH_YY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    birth_md = models.CharField(db_column='BIRTH_MD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    inactive_yn = models.CharField(db_column='INACTIVE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fnl_shop_cd = models.CharField(db_column='FNL_SHOP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_INFO_EX'


class TjsCustInfoInactive(models.Model):
    mno = models.IntegerField(db_column='MNO')  # Field name made lowercase.
    cardcode = models.CharField(db_column='CARDCODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mname = models.CharField(db_column='MNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=6, blank=True, null=True)  # Field name made lowercase.
    mdiv1 = models.SmallIntegerField(db_column='MDIV1', blank=True, null=True)  # Field name made lowercase.
    mdiv2 = models.SmallIntegerField(db_column='MDIV2', blank=True, null=True)  # Field name made lowercase.
    mdiv3 = models.SmallIntegerField(db_column='MDIV3', blank=True, null=True)  # Field name made lowercase.
    mdiv4 = models.SmallIntegerField(db_column='MDIV4', blank=True, null=True)  # Field name made lowercase.
    mdiv5 = models.SmallIntegerField(db_column='MDIV5', blank=True, null=True)  # Field name made lowercase.
    bdiv = models.CharField(db_column='BDIV', max_length=4, blank=True, null=True)  # Field name made lowercase.
    birth = models.CharField(db_column='BIRTH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mzipcode = models.CharField(db_column='MZIPCODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    maddress = models.CharField(db_column='MADDRESS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    marryyn = models.CharField(db_column='MARRYYN', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nation = models.CharField(db_column='NATION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdate = models.CharField(db_column='FDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldate = models.CharField(db_column='LDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdate = models.CharField(db_column='CDATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=30, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    totalcost = models.IntegerField(db_column='TOTALCOST', blank=True, null=True)  # Field name made lowercase.
    mpoint = models.IntegerField(db_column='MPOINT', blank=True, null=True)  # Field name made lowercase.
    bcharge = models.IntegerField(db_column='BCHARGE', blank=True, null=True)  # Field name made lowercase.
    hgcnt = models.IntegerField(db_column='HGCNT', blank=True, null=True)  # Field name made lowercase.
    misoo = models.IntegerField(db_column='MISOO', blank=True, null=True)  # Field name made lowercase.
    smsyn = models.CharField(db_column='SMSYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    visitcnt = models.IntegerField(db_column='VISITCNT', blank=True, null=True)  # Field name made lowercase.
    ddcnt = models.IntegerField(db_column='DDCNT', blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo4 = models.CharField(db_column='ETCINFO4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo5 = models.CharField(db_column='ETCINFO5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo6 = models.CharField(db_column='ETCINFO6', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo7 = models.CharField(db_column='ETCINFO7', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo8 = models.CharField(db_column='ETCINFO8', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo9 = models.CharField(db_column='ETCINFO9', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo10 = models.CharField(db_column='ETCINFO10', max_length=30, blank=True, null=True)  # Field name made lowercase.
    appyn = models.CharField(db_column='APPYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    regid = models.CharField(db_column='REGID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    adjid = models.CharField(db_column='ADJID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adjdate = models.CharField(db_column='ADJDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_INFO_INACTIVE'


class TjsCustInfoSum(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prpd_new_amt = models.DecimalField(db_column='PRPD_NEW_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ticket_cnt = models.DecimalField(db_column='TICKET_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pay_tot_amt = models.DecimalField(db_column='PAY_TOT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vst_cnt = models.DecimalField(db_column='VST_CNT', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    prpd_rt = models.DecimalField(db_column='PRPD_RT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_INFO_SUM'
        unique_together = (('shop_cd', 'cust_cd'),)


class TjsCustInfoSum20210516(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=10)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prpd_new_amt = models.DecimalField(db_column='PRPD_NEW_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ticket_cnt = models.DecimalField(db_column='TICKET_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pay_tot_amt = models.DecimalField(db_column='PAY_TOT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vst_cnt = models.DecimalField(db_column='VST_CNT', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    prpd_rt = models.DecimalField(db_column='PRPD_RT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_INFO_SUM_20210516'


class TjsCustInfoSumWoShop(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prpd_new_amt = models.DecimalField(db_column='PRPD_NEW_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ticket_cnt = models.DecimalField(db_column='TICKET_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pay_tot_amt = models.DecimalField(db_column='PAY_TOT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vst_cnt = models.DecimalField(db_column='VST_CNT', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    prpd_rt = models.DecimalField(db_column='PRPD_RT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_INFO_SUM_WO_SHOP'


class TjsCustMemo(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo_color = models.CharField(db_column='MEMO_COLOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    warn_yn = models.CharField(db_column='WARN_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_MEMO'
        unique_together = (('cust_cd', 'line_no'),)


class TjsCustMemo20210516(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo_color = models.CharField(db_column='MEMO_COLOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    warn_yn = models.CharField(db_column='WARN_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    memo_tp = models.CharField(db_column='MEMO_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_MEMO_20210516'


class TjsCustPrepaidDsgnSum(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    prpd_cd = models.CharField(db_column='PRPD_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_PREPAID_DSGN_SUM'
        unique_together = (('cust_cd', 'line_no'),)


class TjsCustPrepaidList(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=5, decimal_places=0)  # Field name made lowercase.
    io_fg = models.CharField(db_column='IO_FG', max_length=10)  # Field name made lowercase.
    prpd_cd = models.CharField(db_column='PRPD_CD', max_length=10)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_cust_cd = models.CharField(db_column='RCV_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_dsgn_cd = models.CharField(db_column='RCV_DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    use_div_cd = models.CharField(db_column='USE_DIV_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    use_dtm = models.DateTimeField(db_column='USE_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_PREPAID_LIST'


class TjsCustPrepaidList20210516(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=5, decimal_places=0)  # Field name made lowercase.
    io_fg = models.CharField(db_column='IO_FG', max_length=10)  # Field name made lowercase.
    prpd_cd = models.CharField(db_column='PRPD_CD', max_length=10)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_cust_cd = models.CharField(db_column='RCV_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_dsgn_cd = models.CharField(db_column='RCV_DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    use_div_cd = models.CharField(db_column='USE_DIV_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_PREPAID_LIST_20210516'


class TjsCustPrepaidList20210709(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=5, decimal_places=0)  # Field name made lowercase.
    io_fg = models.CharField(db_column='IO_FG', max_length=10)  # Field name made lowercase.
    prpd_cd = models.CharField(db_column='PRPD_CD', max_length=10)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_cust_cd = models.CharField(db_column='RCV_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_dsgn_cd = models.CharField(db_column='RCV_DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    use_div_cd = models.CharField(db_column='USE_DIV_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_PREPAID_LIST_20210709'


class TjsCustPrepaidList20210710(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=5, decimal_places=0)  # Field name made lowercase.
    io_fg = models.CharField(db_column='IO_FG', max_length=10)  # Field name made lowercase.
    prpd_cd = models.CharField(db_column='PRPD_CD', max_length=10)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    rcv_cust_cd = models.CharField(db_column='RCV_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20)  # Field name made lowercase.
    rcv_dsgn_cd = models.CharField(db_column='RCV_DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    use_div_cd = models.CharField(db_column='USE_DIV_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_PREPAID_LIST_20210710'


class TjsCustPrepaidList210417(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=5, decimal_places=0)  # Field name made lowercase.
    io_fg = models.CharField(db_column='IO_FG', max_length=10)  # Field name made lowercase.
    prpd_cd = models.CharField(db_column='PRPD_CD', max_length=10)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_cust_cd = models.CharField(db_column='RCV_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_dsgn_cd = models.CharField(db_column='RCV_DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    use_div_cd = models.CharField(db_column='USE_DIV_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_PREPAID_LIST_210417'


class TjsCustPrepaidMove(models.Model):
    trns_no = models.CharField(db_column='TRNS_NO', primary_key=True, max_length=40)  # Field name made lowercase.
    snd_cust_cd = models.CharField(db_column='SND_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_cust_cd = models.CharField(db_column='RCV_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    snd_dno_cd = models.CharField(db_column='SND_DNO_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_dno_cd = models.CharField(db_column='RCV_DNO_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prepaid_cost = models.DecimalField(db_column='PREPAID_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_PREPAID_MOVE'


class TjsCustPrepaidMove20210516(models.Model):
    trns_no = models.CharField(db_column='TRNS_NO', max_length=40)  # Field name made lowercase.
    trns_tp = models.CharField(db_column='TRNS_TP', max_length=10)  # Field name made lowercase.
    snd_cust_cd = models.CharField(db_column='SND_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_cust_cd = models.CharField(db_column='RCV_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    snd_dno_cd = models.CharField(db_column='SND_DNO_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_dno_cd = models.CharField(db_column='RCV_DNO_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_PREPAID_MOVE_20210516'


class TjsCustPrepaidMst(models.Model):
    prpd_no = models.CharField(db_column='PRPD_NO', primary_key=True, max_length=80)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=40)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=40)  # Field name made lowercase.
    mng_cd = models.CharField(db_column='MNG_CD', max_length=40)  # Field name made lowercase.
    open_dtm = models.DateTimeField(db_column='OPEN_DTM', blank=True, null=True)  # Field name made lowercase.
    close_dtm = models.DateTimeField(db_column='CLOSE_DTM', blank=True, null=True)  # Field name made lowercase.
    close_yn = models.CharField(db_column='CLOSE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=400, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    prpd_cd = models.CharField(db_column='PRPD_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=40)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_PREPAID_MST'


class TjsCustPrepaidSum(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    prpd_cd = models.CharField(db_column='PRPD_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_PREPAID_SUM'
        unique_together = (('cust_cd', 'line_no'),)


class TjsCustPrepaidSum20210412(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    prpd_cd = models.CharField(db_column='PRPD_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_PREPAID_SUM_20210412'


class TjsCustPrepaidSum20210516(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    prpd_cd = models.CharField(db_column='PRPD_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_PREPAID_SUM_20210516'


class TjsCustPrepaidUp(models.Model):
    rseq = models.CharField(db_column='RSEQ', max_length=20)  # Field name made lowercase.
    prpd_no = models.CharField(db_column='PRPD_NO', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=400, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    use_div_cd = models.CharField(db_column='USE_DIV_CD', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_PREPAID_UP'


class TjsCustSearchHst(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_SEARCH_HST'


class TjsCustSign(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    sign_tp = models.CharField(db_column='SIGN_TP', max_length=10)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sign_img = models.BinaryField(db_column='SIGN_IMG', blank=True, null=True)  # Field name made lowercase.
    agr_yn1 = models.CharField(db_column='AGR_YN1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    agr_yn2 = models.CharField(db_column='AGR_YN2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    agr_yn3 = models.CharField(db_column='AGR_YN3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_SIGN'
        unique_together = (('cust_cd', 'sign_tp'),)


class TjsCustSmsSndList(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    shop_nm = models.CharField(db_column='SHOP_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cp_tel = models.CharField(db_column='CP_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_SMS_SND_LIST'


class TjsCustTicket(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    start_dt = models.CharField(db_column='START_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    end_dt = models.CharField(db_column='END_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    org_cnt = models.DecimalField(db_column='ORG_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    use_cnt = models.DecimalField(db_column='USE_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    res_cnt = models.DecimalField(db_column='RES_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_TICKET'
        unique_together = (('cust_cd', 'line_no'),)


class TjsCustTicket20210412(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    start_dt = models.CharField(db_column='START_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    end_dt = models.CharField(db_column='END_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    org_cnt = models.DecimalField(db_column='ORG_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    use_cnt = models.DecimalField(db_column='USE_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    res_cnt = models.DecimalField(db_column='RES_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_TICKET_20210412'


class TjsCustTicket20210525(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    start_dt = models.CharField(db_column='START_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    end_dt = models.CharField(db_column='END_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    org_cnt = models.DecimalField(db_column='ORG_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    use_cnt = models.DecimalField(db_column='USE_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    res_cnt = models.DecimalField(db_column='RES_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_TICKET_20210525'


class TjsCustTicketList(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    use_dtm = models.DateTimeField(db_column='USE_DTM', blank=True, null=True)  # Field name made lowercase.
    use_cnt = models.DecimalField(db_column='USE_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_TICKET_LIST'
        unique_together = (('cust_cd', 'mgmt_no', 'line_no'),)


class TjsCustTicketList20210412(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=10)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    use_dtm = models.DateTimeField(db_column='USE_DTM', blank=True, null=True)  # Field name made lowercase.
    use_cnt = models.DecimalField(db_column='USE_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_TICKET_LIST_20210412'


class TjsCustTicketListTmp(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    line_no = models.BigIntegerField(db_column='LINE_NO', blank=True, null=True)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    use_dtm = models.DateTimeField(db_column='USE_DTM', blank=True, null=True)  # Field name made lowercase.
    use_cnt = models.DecimalField(db_column='USE_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_TICKET_LIST_TMP'


class TjsCustTicketTest(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    start_dt = models.CharField(db_column='START_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    end_dt = models.CharField(db_column='END_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    org_cnt = models.DecimalField(db_column='ORG_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    use_cnt = models.DecimalField(db_column='USE_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    res_cnt = models.DecimalField(db_column='RES_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_CUST_TICKET_TEST'


class TjsDayTimeBase(models.Model):
    line_no = models.BigIntegerField(db_column='LINE_NO', blank=True, null=True)  # Field name made lowercase.
    start_hm = models.CharField(db_column='START_HM', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_DAY_TIME_BASE'


class TjsDiscntMthd(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=40)  # Field name made lowercase.
    discnt_cd = models.CharField(db_column='DISCNT_CD', max_length=10)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_DISCNT_MTHD'
        unique_together = (('shop_cd', 'ord_no', 'discnt_cd'),)


class TjsDsgnNaverScheduleSet(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    start_dt = models.CharField(db_column='START_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    end_dt = models.CharField(db_column='END_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    hldy_yn = models.CharField(db_column='HLDY_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    week_set = models.CharField(db_column='WEEK_SET', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tset = models.CharField(db_column='TSET', max_length=300, blank=True, null=True)  # Field name made lowercase.
    hbit = models.CharField(db_column='HBIT', max_length=48, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_DSGN_NAVER_SCHEDULE_SET'
        unique_together = (('shop_cd', 'dsgn_cd', 'line_no'),)


class TjsEmployee(models.Model):
    emp_no = models.CharField(db_column='EMP_NO', primary_key=True, max_length=40)  # Field name made lowercase.
    emp_nm = models.CharField(db_column='EMP_NM', max_length=80)  # Field name made lowercase.
    nick_nm = models.CharField(db_column='NICK_NM', max_length=80, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ofpos_cd = models.IntegerField(db_column='OFPOS_CD', blank=True, null=True)  # Field name made lowercase.
    ofpos_nm = models.CharField(db_column='OFPOS_NM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ofrp_cd = models.IntegerField(db_column='OFRP_CD', blank=True, null=True)  # Field name made lowercase.
    ofrp_nm = models.CharField(db_column='OFRP_NM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    join_dt = models.CharField(db_column='JOIN_DT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    empl_stat = models.CharField(db_column='EMPL_STAT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EMPLOYEE'
        unique_together = (('emp_no', 'emp_nm'),)


class TjsEmpAuth(models.Model):
    auth_cd = models.CharField(db_column='AUTH_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    auth_nm = models.CharField(db_column='AUTH_NM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EMP_AUTH'


class TjsEmpAuthTmp(models.Model):
    auth_cd = models.CharField(db_column='AUTH_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    auth_nm = models.CharField(db_column='AUTH_NM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EMP_AUTH_TMP'


class TjsEmpChngHis(models.Model):
    emp_no = models.CharField(db_column='EMP_NO', primary_key=True, max_length=40)  # Field name made lowercase.
    shop_cd_bf = models.CharField(db_column='SHOP_CD_BF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    shop_cd_af = models.CharField(db_column='SHOP_CD_AF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ofpos_cd_bf = models.IntegerField(db_column='OFPOS_CD_BF', blank=True, null=True)  # Field name made lowercase.
    ofpos_cd_af = models.IntegerField(db_column='OFPOS_CD_AF', blank=True, null=True)  # Field name made lowercase.
    ofrp_cd_bf = models.IntegerField(db_column='OFRP_CD_BF', blank=True, null=True)  # Field name made lowercase.
    ofrp_cd_af = models.IntegerField(db_column='OFRP_CD_AF', blank=True, null=True)  # Field name made lowercase.
    chng_cd = models.CharField(db_column='CHNG_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EMP_CHNG_HIS'


class TjsEmpTmp(models.Model):
    emp_no = models.CharField(db_column='EMP_NO', max_length=40)  # Field name made lowercase.
    emp_nm = models.CharField(db_column='EMP_NM', max_length=80, blank=True, null=True)  # Field name made lowercase.
    nick_nm = models.CharField(db_column='NICK_NM', max_length=80, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ofpos_cd = models.IntegerField(db_column='OFPOS_CD', blank=True, null=True)  # Field name made lowercase.
    ofpos_nm = models.CharField(db_column='OFPOS_NM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ofrp_cd = models.IntegerField(db_column='OFRP_CD', blank=True, null=True)  # Field name made lowercase.
    ofrp_nm = models.CharField(db_column='OFRP_NM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    join_dt = models.CharField(db_column='JOIN_DT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    empl_stat = models.CharField(db_column='EMPL_STAT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EMP_TMP'


class TjsEquipment(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    eq_cd = models.CharField(db_column='EQ_CD', max_length=20)  # Field name made lowercase.
    eq_nm = models.CharField(db_column='EQ_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mac_adr = models.CharField(db_column='MAC_ADR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ediv = models.CharField(db_column='EDIV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EQUIPMENT'
        unique_together = (('shop_cd', 'eq_cd'),)


class TjsEquipment20210517(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    eq_cd = models.CharField(db_column='EQ_CD', max_length=20)  # Field name made lowercase.
    eq_nm = models.CharField(db_column='EQ_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mac_adr = models.CharField(db_column='MAC_ADR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    div_cd = models.CharField(db_column='DIV_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.CharField(db_column='REG_DTM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.CharField(db_column='UPD_DTM', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EQUIPMENT_20210517'


class TjsEquipmentConfig(models.Model):
    eq_cd = models.CharField(db_column='EQ_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='CLASS', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    info = models.CharField(db_column='INFO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    set1 = models.CharField(db_column='SET1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set2 = models.CharField(db_column='SET2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set3 = models.CharField(db_column='SET3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set4 = models.CharField(db_column='SET4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set5 = models.CharField(db_column='SET5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set6 = models.CharField(db_column='SET6', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set7 = models.CharField(db_column='SET7', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set8 = models.CharField(db_column='SET8', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set9 = models.CharField(db_column='SET9', max_length=700, blank=True, null=True)  # Field name made lowercase.
    set10 = models.CharField(db_column='SET10', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EQUIPMENT_CONFIG'


class TjsEquipmentSub(models.Model):
    eq_cd = models.CharField(db_column='EQ_CD', max_length=20)  # Field name made lowercase.
    div_cd = models.CharField(db_column='DIV_CD', max_length=10)  # Field name made lowercase.
    einfo = models.CharField(db_column='EINFO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usestr = models.CharField(db_column='USESTR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    itface = models.CharField(db_column='ITFACE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    speed = models.CharField(db_column='SPEED', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rtime = models.IntegerField(db_column='RTIME', blank=True, null=True)  # Field name made lowercase.
    setdate = models.CharField(db_column='SETDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc1 = models.CharField(db_column='ETC1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc2 = models.CharField(db_column='ETC2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc3 = models.CharField(db_column='ETC3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regid = models.CharField(db_column='REGID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    adjid = models.CharField(db_column='ADJID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adjdate = models.CharField(db_column='ADJDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EQUIPMENT_SUB'


class TjsEquipConfig(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    eq_cd = models.CharField(db_column='EQ_CD', max_length=20)  # Field name made lowercase.
    ctrl_cd = models.CharField(db_column='CTRL_CD', max_length=50)  # Field name made lowercase.
    ctrl_nm = models.CharField(db_column='CTRL_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    set1 = models.CharField(db_column='SET1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set2 = models.CharField(db_column='SET2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set3 = models.CharField(db_column='SET3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set4 = models.CharField(db_column='SET4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set5 = models.CharField(db_column='SET5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set6 = models.CharField(db_column='SET6', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set7 = models.CharField(db_column='SET7', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set8 = models.CharField(db_column='SET8', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set9 = models.CharField(db_column='SET9', max_length=700, blank=True, null=True)  # Field name made lowercase.
    set10 = models.CharField(db_column='SET10', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EQUIP_CONFIG'
        unique_together = (('shop_cd', 'eq_cd', 'ctrl_cd'),)


class TjsEquipDetail(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    eq_cd = models.CharField(db_column='EQ_CD', max_length=20)  # Field name made lowercase.
    dvc_cd = models.DecimalField(db_column='DVC_CD', max_digits=3, decimal_places=0)  # Field name made lowercase.
    dvc_nm = models.CharField(db_column='DVC_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dvc_dc = models.CharField(db_column='DVC_DC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    intr_cd = models.CharField(db_column='INTR_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    spd_vl = models.CharField(db_column='SPD_VL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rspn_tm = models.IntegerField(db_column='RSPN_TM', blank=True, null=True)  # Field name made lowercase.
    set_dtm = models.DateTimeField(db_column='SET_DTM', blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EQUIP_DETAIL'
        unique_together = (('shop_cd', 'eq_cd', 'dvc_cd'),)


class TjsEquipInfo(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    eq_cd = models.CharField(db_column='EQ_CD', max_length=20)  # Field name made lowercase.
    eq_nm = models.CharField(db_column='EQ_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mac_adr = models.CharField(db_column='MAC_ADR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    div_cd = models.CharField(db_column='DIV_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.CharField(db_column='REG_DTM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.CharField(db_column='UPD_DTM', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EQUIP_INFO'
        unique_together = (('shop_cd', 'eq_cd'),)


class TjsErrLog(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    eq_cd = models.CharField(db_column='EQ_CD', max_length=6, blank=True, null=True)  # Field name made lowercase.
    msg = models.CharField(db_column='MSG', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ERR_LOG'


class TjsEventMas(models.Model):
    evn_cd = models.CharField(db_column='EVN_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    evn_nm = models.CharField(db_column='EVN_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    start_dt = models.CharField(db_column='START_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    end_dt = models.CharField(db_column='END_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EVENT_MAS'


class TjsExtAgncMap(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=40)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=18, decimal_places=0)  # Field name made lowercase.
    map_div_cd = models.CharField(db_column='MAP_DIV_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    agnc_shop_cd = models.CharField(db_column='AGNC_SHOP_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    agnc_dsgn_cd = models.CharField(db_column='AGNC_DSGN_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    map_req_id = models.CharField(db_column='MAP_REQ_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80, blank=True, null=True)  # Field name made lowercase.
    agnc_cd = models.CharField(db_column='AGNC_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    disp_yn = models.CharField(db_column='DISP_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EXT_AGNC_MAP'
        unique_together = (('shop_cd', 'line_no'),)


class TjsExtAgncPay(models.Model):
    pay_id = models.CharField(db_column='PAY_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    pay_line_no = models.DecimalField(db_column='PAY_LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    rsrv_id = models.CharField(db_column='RSRV_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pay_moment = models.CharField(db_column='PAY_MOMENT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_stat = models.CharField(db_column='PAY_STAT', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pay_amount = models.DecimalField(db_column='PAY_AMOUNT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pay_mthd = models.CharField(db_column='PAY_MTHD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pay_order_no = models.CharField(db_column='PAY_ORDER_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paid_price = models.DecimalField(db_column='PAID_PRICE', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    paid_currency = models.CharField(db_column='PAID_CURRENCY', max_length=3, blank=True, null=True)  # Field name made lowercase.
    pay_provider = models.CharField(db_column='PAY_PROVIDER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EXT_AGNC_PAY'
        unique_together = (('pay_id', 'pay_line_no'),)


class TjsExtAgncPayItem(models.Model):
    pay_id = models.CharField(db_column='PAY_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    pay_line_no = models.DecimalField(db_column='PAY_LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    pay_stat = models.CharField(db_column='PAY_STAT', max_length=40, blank=True, null=True)  # Field name made lowercase.
    option_id = models.CharField(db_column='OPTION_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    option_nm = models.CharField(db_column='OPTION_NM', max_length=80, blank=True, null=True)  # Field name made lowercase.
    pay_qt = models.DecimalField(db_column='PAY_QT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pay_type = models.CharField(db_column='PAY_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pay_price = models.DecimalField(db_column='PAY_PRICE', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EXT_AGNC_PAY_ITEM'
        unique_together = (('pay_id', 'pay_line_no'),)


class TjsExtAgncRsrv(models.Model):
    rsrv_id = models.CharField(db_column='RSRV_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    rsrv_tm = models.CharField(db_column='RSRV_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rsrv_stat = models.CharField(db_column='RSRV_STAT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    is_ext_pay = models.CharField(db_column='IS_EXT_PAY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pay_tp_cd = models.CharField(db_column='PAY_TP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rsrv_tp_cd = models.CharField(db_column='RSRV_TP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='PRICE', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    org_price = models.DecimalField(db_column='ORG_PRICE', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_price = models.DecimalField(db_column='RFND_PRICE', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rsrv_price = models.DecimalField(db_column='RSRV_PRICE', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rsrv_qty = models.DecimalField(db_column='RSRV_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EXT_AGNC_RSRV'


class TjsExtAgncRsrvMenu(models.Model):
    rsrv_id = models.CharField(db_column='RSRV_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=18, decimal_places=0)  # Field name made lowercase.
    option_id = models.CharField(db_column='OPTION_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    option_nm = models.CharField(db_column='OPTION_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    rsrv_qty = models.DecimalField(db_column='RSRV_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='PRICE', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    norm_price = models.DecimalField(db_column='NORM_PRICE', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EXT_AGNC_RSRV_MENU'
        unique_together = (('rsrv_id', 'line_no'),)


class TjsExtAgncSchd(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=40)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=40)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=18, decimal_places=0)  # Field name made lowercase.
    day = models.CharField(db_column='DAY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    start_dt = models.CharField(db_column='START_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    end_dt = models.CharField(db_column='END_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    week_days = models.CharField(db_column='WEEK_DAYS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hour_bit = models.CharField(db_column='HOUR_BIT', max_length=48, blank=True, null=True)  # Field name made lowercase.
    is_business_day = models.CharField(db_column='IS_BUSINESS_DAY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    schedule_id = models.CharField(db_column='SCHEDULE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    agnc_cd = models.CharField(db_column='AGNC_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_EXT_AGNC_SCHD'
        unique_together = (('shop_cd', 'dsgn_cd', 'line_no'),)


class TjsFingerPrints(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    fingerindex = models.IntegerField(db_column='FINGERINDEX')  # Field name made lowercase.
    template1 = models.BinaryField(db_column='TEMPLATE1', blank=True, null=True)  # Field name made lowercase.
    template2 = models.BinaryField(db_column='TEMPLATE2', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_FINGER_PRINTS'
        unique_together = (('user_id', 'fingerindex'),)


class TjsHldy(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    user_tp = models.CharField(db_column='USER_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hldy_nm = models.CharField(db_column='HLDY_NM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    holy_dt = models.CharField(db_column='HOLY_DT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    start_dt = models.CharField(db_column='START_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    end_dt = models.CharField(db_column='END_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    start_hm = models.CharField(db_column='START_HM', max_length=5, blank=True, null=True)  # Field name made lowercase.
    end_hm = models.CharField(db_column='END_HM', max_length=5, blank=True, null=True)  # Field name made lowercase.
    all_day_yn = models.CharField(db_column='ALL_DAY_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_HLDY'
        unique_together = (('shop_cd', 'dsgn_cd', 'line_no'),)


class TjsHldyBas(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    user_tp = models.CharField(db_column='USER_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hldy_info = models.CharField(db_column='HLDY_INFO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    hldy_nm = models.CharField(db_column='HLDY_NM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    week_set = models.CharField(db_column='WEEK_SET', max_length=6, blank=True, null=True)  # Field name made lowercase.
    day_set = models.CharField(db_column='DAY_SET', max_length=7, blank=True, null=True)  # Field name made lowercase.
    hbit = models.CharField(db_column='HBIT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    dflt_yn = models.CharField(db_column='DFLT_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    start_tm = models.CharField(db_column='START_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    end_tm = models.CharField(db_column='END_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_HLDY_BAS'
        unique_together = (('shop_cd', 'dsgn_cd', 'line_no'),)


class TjsHldyBasDsgn(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    week_set = models.CharField(db_column='WEEK_SET', max_length=6, blank=True, null=True)  # Field name made lowercase.
    day_set = models.CharField(db_column='DAY_SET', max_length=7, blank=True, null=True)  # Field name made lowercase.
    hbit = models.CharField(db_column='HBIT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_HLDY_BAS_DSGN'
        unique_together = (('shop_cd', 'dsgn_cd', 'line_no'),)


class TjsHldyBasShop(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    week_set = models.CharField(db_column='WEEK_SET', max_length=6, blank=True, null=True)  # Field name made lowercase.
    day_set = models.CharField(db_column='DAY_SET', max_length=7, blank=True, null=True)  # Field name made lowercase.
    hbit = models.CharField(db_column='HBIT', max_length=48, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_HLDY_BAS_SHOP'
        unique_together = (('shop_cd', 'line_no'),)


class TjsHldyDsgn(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    start_dt = models.CharField(db_column='START_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    end_dt = models.CharField(db_column='END_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    start_hm = models.CharField(db_column='START_HM', max_length=5, blank=True, null=True)  # Field name made lowercase.
    end_hm = models.CharField(db_column='END_HM', max_length=5, blank=True, null=True)  # Field name made lowercase.
    all_day_yn = models.CharField(db_column='ALL_DAY_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_HLDY_DSGN'


class TjsHldyShop(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    start_dt = models.CharField(db_column='START_DT', max_length=8)  # Field name made lowercase.
    end_dt = models.CharField(db_column='END_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_HLDY_SHOP'
        unique_together = (('shop_cd', 'start_dt'),)


class TjsHsSalesxcorp(models.Model):
    cpcode = models.SmallIntegerField(db_column='CPCODE')  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=10)  # Field name made lowercase.
    yno = models.SmallIntegerField(db_column='YNO', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.IntegerField(db_column='TOTALCOST', blank=True, null=True)  # Field name made lowercase.
    finalcost = models.IntegerField(db_column='FINALCOST', blank=True, null=True)  # Field name made lowercase.
    vatax = models.IntegerField(db_column='VATAX', blank=True, null=True)  # Field name made lowercase.
    servicefee = models.IntegerField(db_column='SERVICEFEE', blank=True, null=True)  # Field name made lowercase.
    cash = models.IntegerField(db_column='CASH', blank=True, null=True)  # Field name made lowercase.
    cashr = models.IntegerField(db_column='CASHR', blank=True, null=True)  # Field name made lowercase.
    card = models.IntegerField(db_column='CARD', blank=True, null=True)  # Field name made lowercase.
    cardm = models.IntegerField(db_column='CARDM', blank=True, null=True)  # Field name made lowercase.
    mcharge = models.IntegerField(db_column='MCHARGE', blank=True, null=True)  # Field name made lowercase.
    mpoint = models.IntegerField(db_column='MPOINT', blank=True, null=True)  # Field name made lowercase.
    giftcard = models.IntegerField(db_column='GIFTCARD', blank=True, null=True)  # Field name made lowercase.
    ocost1 = models.IntegerField(db_column='OCOST1', blank=True, null=True)  # Field name made lowercase.
    ocost2 = models.IntegerField(db_column='OCOST2', blank=True, null=True)  # Field name made lowercase.
    ocost3 = models.IntegerField(db_column='OCOST3', blank=True, null=True)  # Field name made lowercase.
    ocost4 = models.IntegerField(db_column='OCOST4', blank=True, null=True)  # Field name made lowercase.
    ocost5 = models.IntegerField(db_column='OCOST5', blank=True, null=True)  # Field name made lowercase.
    ocost6 = models.IntegerField(db_column='OCOST6', blank=True, null=True)  # Field name made lowercase.
    ocost7 = models.IntegerField(db_column='OCOST7', blank=True, null=True)  # Field name made lowercase.
    ocost8 = models.IntegerField(db_column='OCOST8', blank=True, null=True)  # Field name made lowercase.
    opoint1 = models.IntegerField(db_column='OPOINT1', blank=True, null=True)  # Field name made lowercase.
    opoint2 = models.IntegerField(db_column='OPOINT2', blank=True, null=True)  # Field name made lowercase.
    opoint3 = models.IntegerField(db_column='OPOINT3', blank=True, null=True)  # Field name made lowercase.
    opoint4 = models.IntegerField(db_column='OPOINT4', blank=True, null=True)  # Field name made lowercase.
    opoint5 = models.IntegerField(db_column='OPOINT5', blank=True, null=True)  # Field name made lowercase.
    opoint6 = models.IntegerField(db_column='OPOINT6', blank=True, null=True)  # Field name made lowercase.
    opoint7 = models.IntegerField(db_column='OPOINT7', blank=True, null=True)  # Field name made lowercase.
    opoint8 = models.IntegerField(db_column='OPOINT8', blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gcash = models.IntegerField(db_column='GCASH', blank=True, null=True)  # Field name made lowercase.
    gcard = models.IntegerField(db_column='GCARD', blank=True, null=True)  # Field name made lowercase.
    getc = models.IntegerField(db_column='GETC', blank=True, null=True)  # Field name made lowercase.
    bcharge = models.IntegerField(db_column='BCHARGE', blank=True, null=True)  # Field name made lowercase.
    tcharge = models.IntegerField(db_column='TCHARGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_HS_SALESxCORP'


class TjsHsSalesxcorpxd(models.Model):
    cpcode = models.SmallIntegerField(db_column='CPCODE')  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=10)  # Field name made lowercase.
    dno = models.CharField(db_column='DNO', max_length=10)  # Field name made lowercase.
    dname = models.CharField(db_column='DNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    yno = models.SmallIntegerField(db_column='YNO', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.IntegerField(db_column='TOTALCOST', blank=True, null=True)  # Field name made lowercase.
    finalcost = models.IntegerField(db_column='FINALCOST', blank=True, null=True)  # Field name made lowercase.
    vatax = models.IntegerField(db_column='VATAX', blank=True, null=True)  # Field name made lowercase.
    servicefee = models.IntegerField(db_column='SERVICEFEE', blank=True, null=True)  # Field name made lowercase.
    cash = models.IntegerField(db_column='CASH', blank=True, null=True)  # Field name made lowercase.
    cashr = models.IntegerField(db_column='CASHR', blank=True, null=True)  # Field name made lowercase.
    card = models.IntegerField(db_column='CARD', blank=True, null=True)  # Field name made lowercase.
    cardm = models.IntegerField(db_column='CARDM', blank=True, null=True)  # Field name made lowercase.
    mcharge = models.IntegerField(db_column='MCHARGE', blank=True, null=True)  # Field name made lowercase.
    mpoint = models.IntegerField(db_column='MPOINT', blank=True, null=True)  # Field name made lowercase.
    giftcard = models.IntegerField(db_column='GIFTCARD', blank=True, null=True)  # Field name made lowercase.
    ocost1 = models.IntegerField(db_column='OCOST1', blank=True, null=True)  # Field name made lowercase.
    ocost2 = models.IntegerField(db_column='OCOST2', blank=True, null=True)  # Field name made lowercase.
    ocost3 = models.IntegerField(db_column='OCOST3', blank=True, null=True)  # Field name made lowercase.
    ocost4 = models.IntegerField(db_column='OCOST4', blank=True, null=True)  # Field name made lowercase.
    ocost5 = models.IntegerField(db_column='OCOST5', blank=True, null=True)  # Field name made lowercase.
    ocost6 = models.IntegerField(db_column='OCOST6', blank=True, null=True)  # Field name made lowercase.
    ocost7 = models.IntegerField(db_column='OCOST7', blank=True, null=True)  # Field name made lowercase.
    ocost8 = models.IntegerField(db_column='OCOST8', blank=True, null=True)  # Field name made lowercase.
    opoint1 = models.IntegerField(db_column='OPOINT1', blank=True, null=True)  # Field name made lowercase.
    opoint2 = models.IntegerField(db_column='OPOINT2', blank=True, null=True)  # Field name made lowercase.
    opoint3 = models.IntegerField(db_column='OPOINT3', blank=True, null=True)  # Field name made lowercase.
    opoint4 = models.IntegerField(db_column='OPOINT4', blank=True, null=True)  # Field name made lowercase.
    opoint5 = models.IntegerField(db_column='OPOINT5', blank=True, null=True)  # Field name made lowercase.
    opoint6 = models.IntegerField(db_column='OPOINT6', blank=True, null=True)  # Field name made lowercase.
    opoint7 = models.IntegerField(db_column='OPOINT7', blank=True, null=True)  # Field name made lowercase.
    opoint8 = models.IntegerField(db_column='OPOINT8', blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gcash = models.IntegerField(db_column='GCASH', blank=True, null=True)  # Field name made lowercase.
    gcard = models.IntegerField(db_column='GCARD', blank=True, null=True)  # Field name made lowercase.
    getc = models.IntegerField(db_column='GETC', blank=True, null=True)  # Field name made lowercase.
    bcharge = models.IntegerField(db_column='BCHARGE', blank=True, null=True)  # Field name made lowercase.
    tcharge = models.IntegerField(db_column='TCHARGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_HS_SALESxCORPxD'


class TjsHsSalesxjumpan(models.Model):
    cpcode = models.SmallIntegerField(db_column='CPCODE')  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=10)  # Field name made lowercase.
    scode = models.CharField(db_column='SCODE', max_length=10)  # Field name made lowercase.
    yno = models.SmallIntegerField(db_column='YNO', blank=True, null=True)  # Field name made lowercase.
    tcnt = models.IntegerField(db_column='TCNT', blank=True, null=True)  # Field name made lowercase.
    tcost = models.IntegerField(db_column='TCOST', blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tcash = models.IntegerField(db_column='TCASH', blank=True, null=True)  # Field name made lowercase.
    tcard = models.IntegerField(db_column='TCARD', blank=True, null=True)  # Field name made lowercase.
    tcashr = models.IntegerField(db_column='TCASHR', blank=True, null=True)  # Field name made lowercase.
    tcardm = models.IntegerField(db_column='TCARDM', blank=True, null=True)  # Field name made lowercase.
    tmcharge = models.IntegerField(db_column='TMCHARGE', blank=True, null=True)  # Field name made lowercase.
    tocost1 = models.IntegerField(db_column='TOCOST1', blank=True, null=True)  # Field name made lowercase.
    tocost2 = models.IntegerField(db_column='TOCOST2', blank=True, null=True)  # Field name made lowercase.
    tocost3 = models.IntegerField(db_column='TOCOST3', blank=True, null=True)  # Field name made lowercase.
    tocost4 = models.IntegerField(db_column='TOCOST4', blank=True, null=True)  # Field name made lowercase.
    tocost5 = models.IntegerField(db_column='TOCOST5', blank=True, null=True)  # Field name made lowercase.
    tocost6 = models.IntegerField(db_column='TOCOST6', blank=True, null=True)  # Field name made lowercase.
    tocost7 = models.IntegerField(db_column='TOCOST7', blank=True, null=True)  # Field name made lowercase.
    tocost8 = models.IntegerField(db_column='TOCOST8', blank=True, null=True)  # Field name made lowercase.
    dcash = models.IntegerField(db_column='DCASH', blank=True, null=True)  # Field name made lowercase.
    dcard = models.IntegerField(db_column='DCARD', blank=True, null=True)  # Field name made lowercase.
    jcash = models.IntegerField(db_column='JCASH', blank=True, null=True)  # Field name made lowercase.
    jcard = models.IntegerField(db_column='JCARD', blank=True, null=True)  # Field name made lowercase.
    scash = models.IntegerField(db_column='SCASH', blank=True, null=True)  # Field name made lowercase.
    scard = models.IntegerField(db_column='SCARD', blank=True, null=True)  # Field name made lowercase.
    tricost = models.IntegerField(db_column='TRICOST', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_HS_SALESxJUMPAN'


class TjsHsSalesxmember(models.Model):
    cpcode = models.SmallIntegerField(db_column='CPCODE')  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=10)  # Field name made lowercase.
    yno = models.SmallIntegerField(db_column='YNO', blank=True, null=True)  # Field name made lowercase.
    acnt = models.IntegerField(db_column='ACNT', blank=True, null=True)  # Field name made lowercase.
    aprice = models.IntegerField(db_column='APRICE', blank=True, null=True)  # Field name made lowercase.
    bcnt = models.IntegerField(db_column='BCNT', blank=True, null=True)  # Field name made lowercase.
    bprice = models.IntegerField(db_column='BPRICE', blank=True, null=True)  # Field name made lowercase.
    ccnt = models.IntegerField(db_column='CCNT', blank=True, null=True)  # Field name made lowercase.
    cprice = models.IntegerField(db_column='CPRICE', blank=True, null=True)  # Field name made lowercase.
    dcnt = models.IntegerField(db_column='DCNT', blank=True, null=True)  # Field name made lowercase.
    dprice = models.IntegerField(db_column='DPRICE', blank=True, null=True)  # Field name made lowercase.
    ecnt = models.IntegerField(db_column='ECNT', blank=True, null=True)  # Field name made lowercase.
    eprice = models.IntegerField(db_column='EPRICE', blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_HS_SALESxMEMBER'


class TjsHsSalesxmemberxd(models.Model):
    cpcode = models.SmallIntegerField(db_column='CPCODE')  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=10)  # Field name made lowercase.
    dno = models.CharField(db_column='DNO', max_length=10)  # Field name made lowercase.
    dname = models.CharField(db_column='DNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    yno = models.SmallIntegerField(db_column='YNO', blank=True, null=True)  # Field name made lowercase.
    acnt = models.IntegerField(db_column='ACNT', blank=True, null=True)  # Field name made lowercase.
    aprice = models.IntegerField(db_column='APRICE', blank=True, null=True)  # Field name made lowercase.
    bcnt = models.IntegerField(db_column='BCNT', blank=True, null=True)  # Field name made lowercase.
    bprice = models.IntegerField(db_column='BPRICE', blank=True, null=True)  # Field name made lowercase.
    ccnt = models.IntegerField(db_column='CCNT', blank=True, null=True)  # Field name made lowercase.
    cprice = models.IntegerField(db_column='CPRICE', blank=True, null=True)  # Field name made lowercase.
    dcnt = models.IntegerField(db_column='DCNT', blank=True, null=True)  # Field name made lowercase.
    dprice = models.IntegerField(db_column='DPRICE', blank=True, null=True)  # Field name made lowercase.
    ecnt = models.IntegerField(db_column='ECNT', blank=True, null=True)  # Field name made lowercase.
    eprice = models.IntegerField(db_column='EPRICE', blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_HS_SALESxMEMBERxD'


class TjsInterfaceHis(models.Model):
    interface_id = models.CharField(db_column='INTERFACE_ID', max_length=30)  # Field name made lowercase.
    snd_rcv_div = models.CharField(db_column='SND_RCV_DIV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    contents = models.TextField(db_column='CONTENTS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    if_stat_cd = models.CharField(db_column='IF_STAT_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    stat_msg = models.CharField(db_column='STAT_MSG', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_INTERFACE_HIS'


class TjsItem(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20)  # Field name made lowercase.
    item_nm = models.CharField(db_column='ITEM_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    item_unit = models.CharField(db_column='ITEM_UNIT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_std = models.CharField(db_column='ITEM_STD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_prc = models.DecimalField(db_column='ITEM_PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    item_grp_cd = models.CharField(db_column='ITEM_GRP_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_div_cd = models.CharField(db_column='ITEM_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    item_brcd = models.CharField(db_column='ITEM_BRCD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    prnt_item_cd = models.CharField(db_column='PRNT_ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prnt_cd = models.CharField(db_column='PRNT_CD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vat_cd = models.CharField(db_column='VAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    srvc_chrg = models.DecimalField(db_column='SRVC_CHRG', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    item_tp = models.CharField(db_column='ITEM_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    item_cnt = models.DecimalField(db_column='ITEM_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    font_color = models.CharField(db_column='FONT_COLOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    discnt_yn = models.CharField(db_column='DISCNT_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prpd_yn = models.CharField(db_column='PRPD_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    point_save_yn = models.CharField(db_column='POINT_SAVE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    point_save_rt = models.DecimalField(db_column='POINT_SAVE_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    point_use_yn = models.CharField(db_column='POINT_USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    disp_yn = models.CharField(db_column='DISP_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    exp_yn = models.CharField(db_column='EXP_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    exp_dy = models.DecimalField(db_column='EXP_DY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ITEM'


class TjsItemDsgnH(models.Model):
    dsgn_cd = models.CharField(db_column='DSGN_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    menu_cd = models.CharField(db_column='MENU_CD', max_length=20)  # Field name made lowercase.
    menu_nm = models.CharField(db_column='MENU_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ITEM_DSGN_H'
        unique_together = (('dsgn_cd', 'menu_cd'),)


class TjsItemDsgnL(models.Model):
    dsgn_cd = models.CharField(db_column='DSGN_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    menu_cd = models.CharField(db_column='MENU_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_prc = models.DecimalField(db_column='ITEM_PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ITEM_DSGN_L'
        unique_together = (('dsgn_cd', 'menu_cd', 'line_no'),)


class TjsItemGrp(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    item_grp_cd = models.CharField(db_column='ITEM_GRP_CD', max_length=20)  # Field name made lowercase.
    item_grp_nm = models.CharField(db_column='ITEM_GRP_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    item_div_cd = models.CharField(db_column='ITEM_DIV_CD', max_length=10)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=5, decimal_places=0)  # Field name made lowercase.
    sys_yn = models.CharField(db_column='SYS_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ITEM_GRP'


class TjsItemGrpTmp(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    item_grp_cd = models.CharField(db_column='ITEM_GRP_CD', max_length=20)  # Field name made lowercase.
    item_grp_nm = models.CharField(db_column='ITEM_GRP_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    item_div_cd = models.CharField(db_column='ITEM_DIV_CD', max_length=10)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=5, decimal_places=0)  # Field name made lowercase.
    sys_yn = models.CharField(db_column='SYS_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ITEM_GRP_TMP'


class TjsItemPrice(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20)  # Field name made lowercase.
    item_prc = models.DecimalField(db_column='ITEM_PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ITEM_PRICE'
        unique_together = (('shop_cd', 'item_cd'),)


class TjsItemShopPrice(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=10)  # Field name made lowercase.
    item_prc = models.CharField(db_column='ITEM_PRC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ITEM_SHOP_PRICE'
        unique_together = (('shop_cd', 'item_cd'),)


class TjsItemSub(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20)  # Field name made lowercase.
    item_sub_no = models.DecimalField(db_column='ITEM_SUB_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    sub_nm = models.CharField(db_column='SUB_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    item_prc = models.DecimalField(db_column='ITEM_PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    show_yn = models.CharField(db_column='SHOW_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    discnt_yn = models.CharField(db_column='DISCNT_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prpd_yn = models.CharField(db_column='PRPD_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ITEM_SUB'


class TjsItemTktBak20210519(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20)  # Field name made lowercase.
    item_nm = models.CharField(db_column='ITEM_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    item_unit = models.CharField(db_column='ITEM_UNIT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_std = models.CharField(db_column='ITEM_STD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_prc = models.DecimalField(db_column='ITEM_PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    item_grp_cd = models.CharField(db_column='ITEM_GRP_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_div_cd = models.CharField(db_column='ITEM_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    item_brcd = models.CharField(db_column='ITEM_BRCD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    prnt_item_cd = models.CharField(db_column='PRNT_ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prnt_cd = models.CharField(db_column='PRNT_CD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vat_cd = models.CharField(db_column='VAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    srvc_chrg = models.DecimalField(db_column='SRVC_CHRG', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    item_tp = models.CharField(db_column='ITEM_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    item_cnt = models.DecimalField(db_column='ITEM_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    font_color = models.CharField(db_column='FONT_COLOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    discnt_yn = models.CharField(db_column='DISCNT_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prpd_yn = models.CharField(db_column='PRPD_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    point_save_yn = models.CharField(db_column='POINT_SAVE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    point_save_rt = models.DecimalField(db_column='POINT_SAVE_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    point_use_yn = models.CharField(db_column='POINT_USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    disp_yn = models.CharField(db_column='DISP_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    exp_yn = models.CharField(db_column='EXP_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    exp_dy = models.DecimalField(db_column='EXP_DY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ITEM_TKT_BAK_20210519'


class TjsLoginHst(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    login_dtm = models.DateTimeField(db_column='LOGIN_DTM', blank=True, null=True)  # Field name made lowercase.
    login_div_cd = models.CharField(db_column='LOGIN_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    eq_cd = models.CharField(db_column='EQ_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ip_in_adr = models.CharField(db_column='IP_IN_ADR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ip_ex_adr = models.CharField(db_column='IP_EX_ADR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mac_adr = models.CharField(db_column='MAC_ADR', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_LOGIN_HST'


class TjsMemberchehyangBk(models.Model):
    mno = models.FloatField(db_column='MNO', blank=True, null=True)  # Field name made lowercase.
    carno = models.CharField(db_column='CARNO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    drink = models.CharField(db_column='DRINK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shamptek = models.CharField(db_column='SHAMPTEK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shampinfo = models.CharField(db_column='SHAMPINFO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipinfo = models.CharField(db_column='TIPINFO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    etcinfo4 = models.CharField(db_column='ETCINFO4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    etcinfo5 = models.CharField(db_column='ETCINFO5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    appyn = models.CharField(db_column='APPYN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    adjid = models.CharField(db_column='ADJID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    adjdate = models.DateTimeField(db_column='ADJDATE', blank=True, null=True)  # Field name made lowercase.
    regid = models.CharField(db_column='REGID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='REGDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_MEMBERCHEHYANG_BK$'


class TjsMemberinfo20210531(models.Model):
    mno = models.IntegerField(db_column='MNO')  # Field name made lowercase.
    cardcode = models.CharField(db_column='CARDCODE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mname = models.CharField(db_column='MNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=6, blank=True, null=True)  # Field name made lowercase.
    mdiv1 = models.SmallIntegerField(db_column='MDIV1', blank=True, null=True)  # Field name made lowercase.
    mdiv2 = models.SmallIntegerField(db_column='MDIV2', blank=True, null=True)  # Field name made lowercase.
    mdiv3 = models.SmallIntegerField(db_column='MDIV3', blank=True, null=True)  # Field name made lowercase.
    mdiv4 = models.SmallIntegerField(db_column='MDIV4', blank=True, null=True)  # Field name made lowercase.
    mdiv5 = models.SmallIntegerField(db_column='MDIV5', blank=True, null=True)  # Field name made lowercase.
    bdiv = models.CharField(db_column='BDIV', max_length=4, blank=True, null=True)  # Field name made lowercase.
    birth = models.CharField(db_column='BIRTH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mzipcode = models.CharField(db_column='MZIPCODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    maddress = models.CharField(db_column='MADDRESS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    marryyn = models.CharField(db_column='MARRYYN', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nation = models.CharField(db_column='NATION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fdate = models.CharField(db_column='FDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ldate = models.CharField(db_column='LDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdate = models.CharField(db_column='CDATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=30, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    totalcost = models.IntegerField(db_column='TOTALCOST', blank=True, null=True)  # Field name made lowercase.
    mpoint = models.IntegerField(db_column='MPOINT', blank=True, null=True)  # Field name made lowercase.
    bcharge = models.IntegerField(db_column='BCHARGE', blank=True, null=True)  # Field name made lowercase.
    hgcnt = models.IntegerField(db_column='HGCNT', blank=True, null=True)  # Field name made lowercase.
    misoo = models.IntegerField(db_column='MISOO', blank=True, null=True)  # Field name made lowercase.
    smsyn = models.CharField(db_column='SMSYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    visitcnt = models.IntegerField(db_column='VISITCNT', blank=True, null=True)  # Field name made lowercase.
    ddcnt = models.IntegerField(db_column='DDCNT', blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo4 = models.CharField(db_column='ETCINFO4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo5 = models.CharField(db_column='ETCINFO5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo6 = models.CharField(db_column='ETCINFO6', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo7 = models.CharField(db_column='ETCINFO7', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo8 = models.CharField(db_column='ETCINFO8', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo9 = models.CharField(db_column='ETCINFO9', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo10 = models.CharField(db_column='ETCINFO10', max_length=30, blank=True, null=True)  # Field name made lowercase.
    appyn = models.CharField(db_column='APPYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    regid = models.CharField(db_column='REGID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    adjid = models.CharField(db_column='ADJID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adjdate = models.CharField(db_column='ADJDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_MEMBERINFO_20210531'


class TjsMemo(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    memo_no = models.CharField(db_column='MEMO_NO', max_length=20)  # Field name made lowercase.
    memo_div_cd = models.CharField(db_column='MEMO_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contents = models.TextField(db_column='CONTENTS', blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_MEMO'
        unique_together = (('shop_cd', 'memo_no'),)


class TjsMmenu(models.Model):
    menu_cd = models.CharField(db_column='MENU_CD', primary_key=True, max_length=30)  # Field name made lowercase.
    menu_nm = models.CharField(db_column='MENU_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    module_cd = models.CharField(db_column='MODULE_CD', max_length=6, blank=True, null=True)  # Field name made lowercase.
    window_nm = models.CharField(db_column='WINDOW_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    file_nm = models.CharField(db_column='FILE_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    menu_fg = models.CharField(db_column='MENU_FG', max_length=6, blank=True, null=True)  # Field name made lowercase.
    parent_menu_cd = models.CharField(db_column='PARENT_MENU_CD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_MMENU'


class TjsMngCd(models.Model):
    dmn_id = models.CharField(db_column='DMN_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    cd_val = models.CharField(db_column='CD_VAL', max_length=20)  # Field name made lowercase.
    cd_nm = models.CharField(db_column='CD_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_cd = models.CharField(db_column='REF_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    grp_cd = models.CharField(db_column='GRP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_MNG_CD'
        unique_together = (('dmn_id', 'cd_val'),)


class TjsMngCdTmp(models.Model):
    dmn_id = models.CharField(db_column='DMN_ID', max_length=10)  # Field name made lowercase.
    cd_val = models.CharField(db_column='CD_VAL', max_length=20)  # Field name made lowercase.
    cd_nm = models.CharField(db_column='CD_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_cd = models.CharField(db_column='REF_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    grp_cd = models.CharField(db_column='GRP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_MNG_CD_TMP'


class TjsMngDmn(models.Model):
    dmn_id = models.CharField(db_column='DMN_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    dmn_nm = models.CharField(db_column='DMN_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dmn_kr_nm = models.CharField(db_column='DMN_KR_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_MNG_DMN'


class TjsMoveH(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=40)  # Field name made lowercase.
    ord_dt = models.DateTimeField(db_column='ORD_DT', blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tot_cost = models.DecimalField(db_column='TOT_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tot_vat = models.DecimalField(db_column='TOT_VAT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_MOVE_H'
        unique_together = (('shop_cd', 'ord_no'),)


class TjsMoveL(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ord_div_cd = models.CharField(db_column='ORD_DIV_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_cnt = models.DecimalField(db_column='ITEM_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    item_prc = models.DecimalField(db_column='ITEM_PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    item_amt = models.DecimalField(db_column='ITEM_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_rt = models.DecimalField(db_column='VAT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_amt = models.DecimalField(db_column='VAT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_MOVE_L'
        unique_together = (('shop_cd', 'ord_no', 'ord_line_no'),)


class TjsNaverHairTag(models.Model):
    hair_tag_cd = models.CharField(db_column='HAIR_TAG_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    hair_tag_nm = models.CharField(db_column='HAIR_TAG_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=1)  # Field name made lowercase.
    is_reviewed = models.CharField(db_column='IS_REVIEWED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    is_imp = models.CharField(db_column='IS_IMP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hair_tag_ctg_cd = models.CharField(db_column='HAIR_TAG_CTG_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_NAVER_HAIR_TAG'
        unique_together = (('hair_tag_cd', 'sex'),)


class TjsNaverHairTagCtg(models.Model):
    hair_tag_ctg_cd = models.CharField(db_column='HAIR_TAG_CTG_CD', primary_key=True, max_length=30)  # Field name made lowercase.
    hair_tag_ctg_nm = models.CharField(db_column='HAIR_TAG_CTG_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    max_sel_cnt = models.IntegerField(db_column='MAX_SEL_CNT', blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_NAVER_HAIR_TAG_CTG'


class TjsNaverMap(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=40)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=18, decimal_places=0)  # Field name made lowercase.
    map_div_cd = models.CharField(db_column='MAP_DIV_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    agnc_shop_cd = models.CharField(db_column='AGNC_SHOP_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    agnc_dsgn_cd = models.CharField(db_column='AGNC_DSGN_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    map_req_id = models.CharField(db_column='MAP_REQ_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80, blank=True, null=True)  # Field name made lowercase.
    agnc_cd = models.CharField(db_column='AGNC_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    disp_yn = models.CharField(db_column='DISP_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_NAVER_MAP'


class TjsNotice(models.Model):
    notice_no = models.CharField(db_column='NOTICE_NO', primary_key=True, max_length=20)  # Field name made lowercase.
    notice_div_cd = models.CharField(db_column='NOTICE_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contents = models.TextField(db_column='CONTENTS', blank=True, null=True)  # Field name made lowercase.
    lnk_nm = models.CharField(db_column='LNK_NM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lnk_url = models.CharField(db_column='LNK_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_NOTICE'


class TjsOrderDsgnTmp(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    ord_dt = models.CharField(db_column='ORD_DT', max_length=8)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=40)  # Field name made lowercase.
    dsgn_cnt = models.IntegerField(db_column='DSGN_CNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_DSGN_TMP'
        unique_together = (('shop_cd', 'ord_dt', 'ord_no'),)


class TjsOrderH(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=40)  # Field name made lowercase.
    ord_dt = models.CharField(db_column='ORD_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ord_tp = models.CharField(db_column='ORD_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ord_stat_cd = models.CharField(db_column='ORD_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tp = models.CharField(db_column='CUST_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_qty = models.DecimalField(db_column='CUST_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wait_tm = models.CharField(db_column='WAIT_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trt_tm = models.CharField(db_column='TRT_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trt_mm = models.DecimalField(db_column='TRT_MM', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tot_cost = models.DecimalField(db_column='TOT_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fin_cost = models.DecimalField(db_column='FIN_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_cost = models.DecimalField(db_column='VAT_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ord_info = models.CharField(db_column='ORD_INFO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_no = models.CharField(db_column='RSRV_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    upsale_yn = models.CharField(db_column='UPSALE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_H'
        unique_together = (('shop_cd', 'ord_no'),)


class TjsOrderH20210517(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=40)  # Field name made lowercase.
    ord_dt = models.CharField(db_column='ORD_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ord_tp = models.CharField(db_column='ORD_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ord_stat_cd = models.CharField(db_column='ORD_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tp = models.CharField(db_column='CUST_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_qty = models.DecimalField(db_column='CUST_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wait_tm = models.CharField(db_column='WAIT_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trt_tm = models.CharField(db_column='TRT_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trt_mm = models.DecimalField(db_column='TRT_MM', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tot_cost = models.DecimalField(db_column='TOT_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fin_cost = models.DecimalField(db_column='FIN_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_cost = models.DecimalField(db_column='VAT_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ord_info = models.CharField(db_column='ORD_INFO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_no = models.CharField(db_column='RSRV_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    upsale_yn = models.CharField(db_column='UPSALE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_H_20210517'


class TjsOrderHDel(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=40)  # Field name made lowercase.
    ord_dt = models.CharField(db_column='ORD_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ord_tp = models.CharField(db_column='ORD_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ord_stat_cd = models.CharField(db_column='ORD_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tp = models.CharField(db_column='CUST_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_qty = models.DecimalField(db_column='CUST_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wait_tm = models.CharField(db_column='WAIT_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trt_tm = models.CharField(db_column='TRT_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trt_mm = models.DecimalField(db_column='TRT_MM', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tot_cost = models.DecimalField(db_column='TOT_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fin_cost = models.DecimalField(db_column='FIN_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_cost = models.DecimalField(db_column='VAT_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ord_info = models.CharField(db_column='ORD_INFO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_no = models.CharField(db_column='RSRV_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    upsale_yn = models.CharField(db_column='UPSALE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_H_DEL'


class TjsOrderHOld(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=40)  # Field name made lowercase.
    ord_dt = models.CharField(db_column='ORD_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ord_tp = models.CharField(db_column='ORD_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ord_stat_cd = models.CharField(db_column='ORD_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tp = models.CharField(db_column='CUST_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_qty = models.DecimalField(db_column='CUST_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wait_tm = models.CharField(db_column='WAIT_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trt_tm = models.CharField(db_column='TRT_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trt_mm = models.DecimalField(db_column='TRT_MM', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tot_cost = models.DecimalField(db_column='TOT_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fin_cost = models.DecimalField(db_column='FIN_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_cost = models.DecimalField(db_column='VAT_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ord_info = models.CharField(db_column='ORD_INFO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_no = models.CharField(db_column='RSRV_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    upsale_yn = models.CharField(db_column='UPSALE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_H_OLD'


class TjsOrderHUpdate(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=40)  # Field name made lowercase.
    ord_dt = models.CharField(db_column='ORD_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ord_tp = models.CharField(db_column='ORD_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ord_stat_cd = models.CharField(db_column='ORD_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tp = models.CharField(db_column='CUST_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_qty = models.DecimalField(db_column='CUST_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wait_tm = models.CharField(db_column='WAIT_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trt_tm = models.CharField(db_column='TRT_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trt_mm = models.DecimalField(db_column='TRT_MM', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tot_cost = models.DecimalField(db_column='TOT_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fin_cost = models.DecimalField(db_column='FIN_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_cost = models.DecimalField(db_column='VAT_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ord_info = models.CharField(db_column='ORD_INFO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_no = models.CharField(db_column='RSRV_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    upsale_yn = models.CharField(db_column='UPSALE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_H_UPDATE'


class TjsOrderL(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ord_div_cd = models.CharField(db_column='ORD_DIV_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_sub_no = models.DecimalField(db_column='ITEM_SUB_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    qt = models.DecimalField(db_column='QT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    prc = models.DecimalField(db_column='PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt = models.DecimalField(db_column='AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_amt = models.DecimalField(db_column='DISCNT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_tp = models.CharField(db_column='DISCNT_TP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cou_amt = models.DecimalField(db_column='COU_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fin_amt = models.DecimalField(db_column='FIN_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_rt = models.DecimalField(db_column='VAT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_amt = models.DecimalField(db_column='VAT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_cnt = models.DecimalField(db_column='BASE_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bonus_cnt = models.DecimalField(db_column='BONUS_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tot_cnt = models.DecimalField(db_column='TOT_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_L'
        unique_together = (('shop_cd', 'ord_no', 'ord_line_no'),)


class TjsOrderL20210517(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ord_div_cd = models.CharField(db_column='ORD_DIV_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_sub_no = models.DecimalField(db_column='ITEM_SUB_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    qt = models.DecimalField(db_column='QT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    prc = models.DecimalField(db_column='PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt = models.DecimalField(db_column='AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_amt = models.DecimalField(db_column='DISCNT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_tp = models.CharField(db_column='DISCNT_TP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cou_amt = models.DecimalField(db_column='COU_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fin_amt = models.DecimalField(db_column='FIN_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_rt = models.DecimalField(db_column='VAT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_amt = models.DecimalField(db_column='VAT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_cnt = models.DecimalField(db_column='BASE_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bonus_cnt = models.DecimalField(db_column='BONUS_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tot_cnt = models.DecimalField(db_column='TOT_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_L_20210517'


class TjsOrderLChg(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    chg_no = models.CharField(db_column='CHG_NO', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ord_dt = models.CharField(db_column='ORD_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    chg_tp = models.CharField(db_column='CHG_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_sub_no = models.DecimalField(db_column='ITEM_SUB_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    qt = models.DecimalField(db_column='QT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    prc = models.DecimalField(db_column='PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt = models.DecimalField(db_column='AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_amt = models.DecimalField(db_column='DISCNT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fin_amt = models.DecimalField(db_column='FIN_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_L_CHG'
        unique_together = (('shop_cd', 'chg_no', 'line_no'),)


class TjsOrderLDel(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ord_div_cd = models.CharField(db_column='ORD_DIV_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_sub_no = models.DecimalField(db_column='ITEM_SUB_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    qt = models.DecimalField(db_column='QT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    prc = models.DecimalField(db_column='PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt = models.DecimalField(db_column='AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_amt = models.DecimalField(db_column='DISCNT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_tp = models.CharField(db_column='DISCNT_TP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cou_amt = models.DecimalField(db_column='COU_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fin_amt = models.DecimalField(db_column='FIN_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_rt = models.DecimalField(db_column='VAT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_amt = models.DecimalField(db_column='VAT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_cnt = models.DecimalField(db_column='BASE_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bonus_cnt = models.DecimalField(db_column='BONUS_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tot_cnt = models.DecimalField(db_column='TOT_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_L_DEL'


class TjsOrderLEvent(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=40)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    evn_cd = models.CharField(db_column='EVN_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_L_EVENT'
        unique_together = (('shop_cd', 'ord_no', 'ord_line_no'),)


class TjsOrderLOld(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ord_div_cd = models.CharField(db_column='ORD_DIV_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_sub_no = models.DecimalField(db_column='ITEM_SUB_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    qt = models.DecimalField(db_column='QT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    prc = models.DecimalField(db_column='PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt = models.DecimalField(db_column='AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_amt = models.DecimalField(db_column='DISCNT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_tp = models.CharField(db_column='DISCNT_TP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cou_amt = models.DecimalField(db_column='COU_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fin_amt = models.DecimalField(db_column='FIN_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_rt = models.DecimalField(db_column='VAT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_amt = models.DecimalField(db_column='VAT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_cnt = models.DecimalField(db_column='BASE_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bonus_cnt = models.DecimalField(db_column='BONUS_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tot_cnt = models.DecimalField(db_column='TOT_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_L_OLD'


class TjsOrderOldMemo(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_OLD_MEMO'


class TjsOrderSign(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    slip_no = models.CharField(db_column='SLIP_NO', max_length=40)  # Field name made lowercase.
    sign_tp = models.CharField(db_column='SIGN_TP', max_length=10)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dt = models.CharField(db_column='DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    sign_img = models.BinaryField(db_column='SIGN_IMG', blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_ORDER_SIGN'
        unique_together = (('shop_cd', 'slip_no', 'sign_tp'),)


class TjsOutboundUrl(models.Model):
    interface_id = models.CharField(db_column='INTERFACE_ID', primary_key=True, max_length=30)  # Field name made lowercase.
    line_no = models.IntegerField(db_column='LINE_NO')  # Field name made lowercase.
    env_div = models.CharField(db_column='ENV_DIV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    domain = models.CharField(db_column='DOMAIN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    int_url = models.CharField(db_column='INT_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(db_column='METHOD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cont_type = models.CharField(db_column='CONT_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cmpny_nm = models.CharField(db_column='CMPNY_NM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dsc = models.CharField(db_column='DSC', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_OUTBOUND_URL'
        unique_together = (('interface_id', 'line_no'),)


class TjsPayDiscount(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    discnt_cd = models.CharField(db_column='DISCNT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    grp_cd = models.CharField(db_column='GRP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PAY_DISCOUNT'
        unique_together = (('shop_cd', 'pay_no', 'line_no'),)


class TjsPayException(models.Model):
    excep_no = models.CharField(db_column='EXCEP_NO', primary_key=True, max_length=90)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=80, blank=True, null=True)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=80, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ord_div_cd = models.CharField(db_column='ORD_DIV_CD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    item_sub_no = models.DecimalField(db_column='ITEM_SUB_NO', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    pay_type_cd = models.CharField(db_column='PAY_TYPE_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amt = models.DecimalField(db_column='AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PAY_EXCEPTION'


class TjsPayH(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40)  # Field name made lowercase.
    pay_dt = models.CharField(db_column='PAY_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pay_stat_cd = models.CharField(db_column='PAY_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_type_cd = models.CharField(db_column='PAY_TYPE_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_amt = models.DecimalField(db_column='PAY_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_amt = models.DecimalField(db_column='DISCNT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tot_amt = models.DecimalField(db_column='TOT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_amt = models.DecimalField(db_column='VAT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    apvl_no = models.CharField(db_column='APVL_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PAY_H'
        unique_together = (('shop_cd', 'pay_no'),)


class TjsPayH20210517(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40)  # Field name made lowercase.
    pay_dt = models.CharField(db_column='PAY_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pay_stat_cd = models.CharField(db_column='PAY_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_type_cd = models.CharField(db_column='PAY_TYPE_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_amt = models.DecimalField(db_column='PAY_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_amt = models.DecimalField(db_column='DISCNT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tot_amt = models.DecimalField(db_column='TOT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_amt = models.DecimalField(db_column='VAT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    apvl_no = models.CharField(db_column='APVL_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PAY_H_20210517'


class TjsPayHDel(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40)  # Field name made lowercase.
    pay_dt = models.CharField(db_column='PAY_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pay_stat_cd = models.CharField(db_column='PAY_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_type_cd = models.CharField(db_column='PAY_TYPE_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_amt = models.DecimalField(db_column='PAY_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_amt = models.DecimalField(db_column='DISCNT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tot_amt = models.DecimalField(db_column='TOT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_amt = models.DecimalField(db_column='VAT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    apvl_no = models.CharField(db_column='APVL_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PAY_H_DEL'


class TjsPayHMig(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40)  # Field name made lowercase.
    pay_dt = models.CharField(db_column='PAY_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pay_stat_cd = models.CharField(db_column='PAY_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_type_cd = models.CharField(db_column='PAY_TYPE_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_amt = models.DecimalField(db_column='PAY_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_amt = models.DecimalField(db_column='DISCNT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tot_amt = models.DecimalField(db_column='TOT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_amt = models.DecimalField(db_column='VAT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    apvl_no = models.CharField(db_column='APVL_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PAY_H_MIG'


class TjsPayHUpdate(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40)  # Field name made lowercase.
    pay_dt = models.CharField(db_column='PAY_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pay_stat_cd = models.CharField(db_column='PAY_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_type_cd = models.CharField(db_column='PAY_TYPE_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_amt = models.DecimalField(db_column='PAY_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_amt = models.DecimalField(db_column='DISCNT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tot_amt = models.DecimalField(db_column='TOT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_amt = models.DecimalField(db_column='VAT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    apvl_no = models.CharField(db_column='APVL_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PAY_H_UPDATE'


class TjsPayL(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=20)  # Field name made lowercase.
    pay_line_no = models.DecimalField(db_column='PAY_LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_cnt = models.DecimalField(db_column='ITEM_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    qt = models.DecimalField(db_column='QT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prc = models.DecimalField(db_column='PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt = models.DecimalField(db_column='AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_amt = models.DecimalField(db_column='DISCNT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_rt = models.DecimalField(db_column='VAT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_amt = models.DecimalField(db_column='VAT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tot_amt = models.DecimalField(db_column='TOT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PAY_L'
        unique_together = (('shop_cd', 'pay_no', 'pay_line_no'),)


class TjsPayMthd(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    pay_stat_cd = models.CharField(db_column='PAY_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_type_cd = models.CharField(db_column='PAY_TYPE_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_amt = models.DecimalField(db_column='PAY_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='REF_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_line_no = models.DecimalField(db_column='REF_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    apvl_no = models.CharField(db_column='APVL_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PAY_MTHD'
        unique_together = (('shop_cd', 'pay_no', 'line_no'),)


class TjsPayMthd20210517(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    pay_stat_cd = models.CharField(db_column='PAY_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_type_cd = models.CharField(db_column='PAY_TYPE_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_amt = models.DecimalField(db_column='PAY_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='REF_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_line_no = models.DecimalField(db_column='REF_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    apvl_no = models.CharField(db_column='APVL_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PAY_MTHD_20210517'


class TjsPayMthdDel(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    pay_stat_cd = models.CharField(db_column='PAY_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_type_cd = models.CharField(db_column='PAY_TYPE_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_amt = models.DecimalField(db_column='PAY_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='REF_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_line_no = models.DecimalField(db_column='REF_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    apvl_no = models.CharField(db_column='APVL_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PAY_MTHD_DEL'


class TjsPayMthdOld(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    pay_stat_cd = models.CharField(db_column='PAY_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_type_cd = models.CharField(db_column='PAY_TYPE_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_amt = models.DecimalField(db_column='PAY_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='REF_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_line_no = models.DecimalField(db_column='REF_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    apvl_no = models.CharField(db_column='APVL_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PAY_MTHD_OLD'


class TjsPhnCallList(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    call_dtm = models.DateTimeField(db_column='CALL_DTM', blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    call_stat_cd = models.CharField(db_column='CALL_STAT_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tel_no = models.CharField(db_column='TEL_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PHN_CALL_LIST'


class TjsPrepaidMove(models.Model):
    trns_no = models.CharField(db_column='TRNS_NO', primary_key=True, max_length=40)  # Field name made lowercase.
    trns_dt = models.CharField(db_column='TRNS_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    trns_tp = models.CharField(db_column='TRNS_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    trns_info = models.CharField(db_column='TRNS_INFO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    snd_shop_cd = models.CharField(db_column='SND_SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_shop_cd = models.CharField(db_column='RCV_SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    snd_cust_cd = models.CharField(db_column='SND_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_cust_cd = models.CharField(db_column='RCV_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    snd_dsgn_cd = models.CharField(db_column='SND_DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_dsgn_cd = models.CharField(db_column='RCV_DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_cd = models.CharField(db_column='PRPD_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_PREPAID_MOVE'


class TjsRcptConfigH(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    rcpt_cd = models.CharField(db_column='RCPT_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcpt_nm = models.CharField(db_column='RCPT_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    rcpt_tp = models.CharField(db_column='RCPT_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    detail_dc = models.CharField(db_column='DETAIL_DC', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    rpt_yn = models.CharField(db_column='RPT_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    talk_yn = models.CharField(db_column='TALK_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_RCPT_CONFIG_H'
        unique_together = (('shop_cd', 'line_no'),)


class TjsRsrv(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    rsrv_no = models.CharField(db_column='RSRV_NO', max_length=40)  # Field name made lowercase.
    rsrv_div_cd = models.CharField(db_column='RSRV_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=8)  # Field name made lowercase.
    rsrv_tm = models.CharField(db_column='RSRV_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rsrv_drt_mm = models.DecimalField(db_column='RSRV_DRT_MM', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tel = models.CharField(db_column='CUST_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_qty = models.DecimalField(db_column='CUST_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_cd = models.CharField(db_column='RSRV_MENU_CD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_nm = models.CharField(db_column='RSRV_MENU_NM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_memo = models.CharField(db_column='RSRV_MEMO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rsrv_stat_cd = models.CharField(db_column='RSRV_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_amt = models.DecimalField(db_column='RSRV_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='REF_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_id = models.CharField(db_column='REF_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_RSRV'
        unique_together = (('shop_cd', 'rsrv_no'),)


class TjsRsrv20210412(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    rsrv_no = models.CharField(db_column='RSRV_NO', max_length=40)  # Field name made lowercase.
    rsrv_div_cd = models.CharField(db_column='RSRV_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=8)  # Field name made lowercase.
    rsrv_tm = models.CharField(db_column='RSRV_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rsrv_drt_mm = models.DecimalField(db_column='RSRV_DRT_MM', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tel = models.CharField(db_column='CUST_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_qty = models.DecimalField(db_column='CUST_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_cd = models.CharField(db_column='RSRV_MENU_CD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_nm = models.CharField(db_column='RSRV_MENU_NM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_memo = models.CharField(db_column='RSRV_MEMO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rsrv_stat_cd = models.CharField(db_column='RSRV_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_amt = models.DecimalField(db_column='RSRV_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='REF_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_id = models.CharField(db_column='REF_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_RSRV_20210412'


class TjsRsrv20210516(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    rsrv_no = models.CharField(db_column='RSRV_NO', max_length=40)  # Field name made lowercase.
    rsrv_div_cd = models.CharField(db_column='RSRV_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=8)  # Field name made lowercase.
    rsrv_tm = models.CharField(db_column='RSRV_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rsrv_drt_mm = models.DecimalField(db_column='RSRV_DRT_MM', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tel = models.CharField(db_column='CUST_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_qty = models.DecimalField(db_column='CUST_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_cd = models.CharField(db_column='RSRV_MENU_CD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_nm = models.CharField(db_column='RSRV_MENU_NM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_memo = models.CharField(db_column='RSRV_MEMO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rsrv_stat_cd = models.CharField(db_column='RSRV_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_amt = models.DecimalField(db_column='RSRV_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='REF_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_id = models.CharField(db_column='REF_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_RSRV_20210516'


class TjsRsrv20210520C(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    rsrv_no = models.CharField(db_column='RSRV_NO', max_length=40)  # Field name made lowercase.
    rsrv_div_cd = models.CharField(db_column='RSRV_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=8)  # Field name made lowercase.
    rsrv_tm = models.CharField(db_column='RSRV_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rsrv_drt_mm = models.DecimalField(db_column='RSRV_DRT_MM', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tel = models.CharField(db_column='CUST_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_qty = models.DecimalField(db_column='CUST_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_cd = models.CharField(db_column='RSRV_MENU_CD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_nm = models.CharField(db_column='RSRV_MENU_NM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_memo = models.CharField(db_column='RSRV_MEMO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rsrv_stat_cd = models.CharField(db_column='RSRV_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_amt = models.DecimalField(db_column='RSRV_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='REF_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_id = models.CharField(db_column='REF_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_RSRV_20210520_C'


class TjsRsrvHairTag(models.Model):
    rsrv_no = models.CharField(db_column='RSRV_NO', primary_key=True, max_length=40)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=18, decimal_places=0)  # Field name made lowercase.
    hair_tag_ctg_cd = models.CharField(db_column='HAIR_TAG_CTG_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hair_tag_cd = models.CharField(db_column='HAIR_TAG_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hair_tag_nm = models.CharField(db_column='HAIR_TAG_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_RSRV_HAIR_TAG'
        unique_together = (('rsrv_no', 'line_no'),)


class TjsRsrvMig(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    rsrv_no = models.CharField(db_column='RSRV_NO', max_length=40)  # Field name made lowercase.
    rsrv_div_cd = models.CharField(db_column='RSRV_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=8)  # Field name made lowercase.
    rsrv_tm = models.CharField(db_column='RSRV_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rsrv_drt_mm = models.DecimalField(db_column='RSRV_DRT_MM', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tel = models.CharField(db_column='CUST_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_qty = models.DecimalField(db_column='CUST_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_cd = models.CharField(db_column='RSRV_MENU_CD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_nm = models.CharField(db_column='RSRV_MENU_NM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_memo = models.CharField(db_column='RSRV_MEMO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rsrv_stat_cd = models.CharField(db_column='RSRV_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_amt = models.DecimalField(db_column='RSRV_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='REF_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_id = models.CharField(db_column='REF_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_RSRV_MIG'


class TjsRsrvSet(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=12)  # Field name made lowercase.
    line_no = models.BigIntegerField(db_column='LINE_NO')  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=10)  # Field name made lowercase.
    tset = models.CharField(db_column='TSET', max_length=200, blank=True, null=True)  # Field name made lowercase.
    hbit = models.CharField(db_column='HBIT', max_length=48, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_RSRV_SET'
        unique_together = (('shop_cd', 'dsgn_cd', 'line_no', 'rsrv_dt'),)


class TjsRsrvSet20210516(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=12)  # Field name made lowercase.
    line_no = models.BigIntegerField(db_column='LINE_NO')  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=10)  # Field name made lowercase.
    tset = models.CharField(db_column='TSET', max_length=300, blank=True, null=True)  # Field name made lowercase.
    hbit = models.CharField(db_column='HBIT', max_length=48, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_RSRV_SET_20210516'


class TjsRsrvSet20210531(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=12)  # Field name made lowercase.
    line_no = models.BigIntegerField(db_column='LINE_NO')  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=10)  # Field name made lowercase.
    tset = models.CharField(db_column='TSET', max_length=300, blank=True, null=True)  # Field name made lowercase.
    hbit = models.CharField(db_column='HBIT', max_length=48, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_RSRV_SET_20210531'


class TjsRsrvSetMig(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=10)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=12)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    tset = models.CharField(db_column='TSET', max_length=300, blank=True, null=True)  # Field name made lowercase.
    hbit = models.CharField(db_column='HBIT', max_length=48, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_RSRV_SET_MIG'


class TjsRsrvSetNaver(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=12)  # Field name made lowercase.
    line_no = models.BigIntegerField(db_column='LINE_NO')  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=10)  # Field name made lowercase.
    tset = models.CharField(db_column='TSET', max_length=300, blank=True, null=True)  # Field name made lowercase.
    hbit = models.CharField(db_column='HBIT', max_length=48, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    snd_yn = models.CharField(db_column='SND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_RSRV_SET_NAVER'


class TjsRsrvUpdate(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    rsrv_no = models.CharField(db_column='RSRV_NO', max_length=40)  # Field name made lowercase.
    rsrv_div_cd = models.CharField(db_column='RSRV_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=8)  # Field name made lowercase.
    rsrv_tm = models.CharField(db_column='RSRV_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rsrv_drt_mm = models.DecimalField(db_column='RSRV_DRT_MM', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tel = models.CharField(db_column='CUST_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_qty = models.DecimalField(db_column='CUST_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_cd = models.CharField(db_column='RSRV_MENU_CD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_nm = models.CharField(db_column='RSRV_MENU_NM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_memo = models.CharField(db_column='RSRV_MEMO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rsrv_stat_cd = models.CharField(db_column='RSRV_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_amt = models.DecimalField(db_column='RSRV_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='REF_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_id = models.CharField(db_column='REF_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_RSRV_UPDATE'


class TjsSales(models.Model):
    ordercode = models.CharField(db_column='ORDERCODE', max_length=20)  # Field name made lowercase.
    appyn = models.CharField(db_column='APPYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cstate = models.CharField(db_column='CSTATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    wtime = models.CharField(db_column='WTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    stime = models.CharField(db_column='STIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    refundyn = models.CharField(db_column='REFUNDYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rordercode = models.CharField(db_column='RORDERCODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rdate = models.CharField(db_column='RDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    seqname = models.CharField(db_column='SEQNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wid = models.CharField(db_column='WID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weqname = models.CharField(db_column='WEQNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wdate = models.CharField(db_column='WDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cpcode = models.SmallIntegerField(db_column='CPCODE', blank=True, null=True)  # Field name made lowercase.
    dno = models.CharField(db_column='DNO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    dname = models.CharField(db_column='DNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mno = models.IntegerField(db_column='MNO', blank=True, null=True)  # Field name made lowercase.
    cno = models.CharField(db_column='CNO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gno = models.CharField(db_column='GNO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    totalcost = models.IntegerField(db_column='TOTALCOST', blank=True, null=True)  # Field name made lowercase.
    finalcost = models.IntegerField(db_column='FINALCOST', blank=True, null=True)  # Field name made lowercase.
    vatax = models.IntegerField(db_column='VATAX', blank=True, null=True)  # Field name made lowercase.
    servicefee = models.IntegerField(db_column='SERVICEFEE', blank=True, null=True)  # Field name made lowercase.
    cash = models.IntegerField(db_column='CASH', blank=True, null=True)  # Field name made lowercase.
    cashr = models.IntegerField(db_column='CASHR', blank=True, null=True)  # Field name made lowercase.
    card = models.IntegerField(db_column='CARD', blank=True, null=True)  # Field name made lowercase.
    cardm = models.IntegerField(db_column='CARDM', blank=True, null=True)  # Field name made lowercase.
    mcharge = models.IntegerField(db_column='MCHARGE', blank=True, null=True)  # Field name made lowercase.
    mpoint = models.IntegerField(db_column='MPOINT', blank=True, null=True)  # Field name made lowercase.
    giftcard = models.IntegerField(db_column='GIFTCARD', blank=True, null=True)  # Field name made lowercase.
    misoo = models.IntegerField(db_column='MISOO', blank=True, null=True)  # Field name made lowercase.
    misooinfo = models.CharField(db_column='MISOOINFO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ocost1 = models.IntegerField(db_column='OCOST1', blank=True, null=True)  # Field name made lowercase.
    ocost2 = models.IntegerField(db_column='OCOST2', blank=True, null=True)  # Field name made lowercase.
    ocost3 = models.IntegerField(db_column='OCOST3', blank=True, null=True)  # Field name made lowercase.
    ocost4 = models.IntegerField(db_column='OCOST4', blank=True, null=True)  # Field name made lowercase.
    ocost5 = models.IntegerField(db_column='OCOST5', blank=True, null=True)  # Field name made lowercase.
    ocost6 = models.IntegerField(db_column='OCOST6', blank=True, null=True)  # Field name made lowercase.
    ocost7 = models.IntegerField(db_column='OCOST7', blank=True, null=True)  # Field name made lowercase.
    ocost8 = models.IntegerField(db_column='OCOST8', blank=True, null=True)  # Field name made lowercase.
    opoint1 = models.IntegerField(db_column='OPOINT1', blank=True, null=True)  # Field name made lowercase.
    opoint2 = models.IntegerField(db_column='OPOINT2', blank=True, null=True)  # Field name made lowercase.
    opoint3 = models.IntegerField(db_column='OPOINT3', blank=True, null=True)  # Field name made lowercase.
    opoint4 = models.IntegerField(db_column='OPOINT4', blank=True, null=True)  # Field name made lowercase.
    opoint5 = models.IntegerField(db_column='OPOINT5', blank=True, null=True)  # Field name made lowercase.
    opoint6 = models.IntegerField(db_column='OPOINT6', blank=True, null=True)  # Field name made lowercase.
    opoint7 = models.IntegerField(db_column='OPOINT7', blank=True, null=True)  # Field name made lowercase.
    opoint8 = models.IntegerField(db_column='OPOINT8', blank=True, null=True)  # Field name made lowercase.
    discnt1 = models.CharField(db_column='DISCNT1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    discntinfo1 = models.CharField(db_column='DISCNTINFO1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt2 = models.CharField(db_column='DISCNT2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo2 = models.CharField(db_column='DISCNTINFO2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt3 = models.CharField(db_column='DISCNT3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo3 = models.CharField(db_column='DISCNTINFO3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt4 = models.CharField(db_column='DISCNT4', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo4 = models.CharField(db_column='DISCNTINFO4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt5 = models.CharField(db_column='DISCNT5', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo5 = models.CharField(db_column='DISCNTINFO5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt6 = models.CharField(db_column='DISCNT6', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo6 = models.CharField(db_column='DISCNTINFO6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt7 = models.CharField(db_column='DISCNT7', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo7 = models.CharField(db_column='DISCNTINFO7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt8 = models.CharField(db_column='DISCNT8', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo8 = models.CharField(db_column='DISCNTINFO8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smemo = models.CharField(db_column='SMEMO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SALES'


class TjsSalesgoods(models.Model):
    regno = models.IntegerField(db_column='REGNO')  # Field name made lowercase.
    ordercode = models.CharField(db_column='ORDERCODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sdiv = models.CharField(db_column='SDIV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='SCODE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sname = models.CharField(db_column='SNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dno = models.CharField(db_column='DNO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    dname = models.CharField(db_column='DNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wid = models.CharField(db_column='WID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weqname = models.CharField(db_column='WEQNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wdate = models.CharField(db_column='WDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gno = models.IntegerField(db_column='GNO', blank=True, null=True)  # Field name made lowercase.
    gname = models.CharField(db_column='GNAME', max_length=80, blank=True, null=True)  # Field name made lowercase.
    gcnt = models.SmallIntegerField(db_column='GCNT', blank=True, null=True)  # Field name made lowercase.
    gprice = models.IntegerField(db_column='GPRICE', blank=True, null=True)  # Field name made lowercase.
    ginprice = models.IntegerField(db_column='GINPRICE', blank=True, null=True)  # Field name made lowercase.
    pumno = models.CharField(db_column='PUMNO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    appyn = models.CharField(db_column='APPYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dyn = models.CharField(db_column='DYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    psyn = models.CharField(db_column='PSYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    puyn = models.CharField(db_column='PUYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    discntyn = models.CharField(db_column='DISCNTYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    giveyn = models.CharField(db_column='GIVEYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    transyn = models.CharField(db_column='TRANSYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etcyn1 = models.CharField(db_column='ETCYN1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etcyn2 = models.CharField(db_column='ETCYN2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etcyn3 = models.CharField(db_column='ETCYN3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etcyn4 = models.CharField(db_column='ETCYN4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etcyn5 = models.CharField(db_column='ETCYN5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    etcinfo4 = models.CharField(db_column='ETCINFO4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    etcinfo5 = models.CharField(db_column='ETCINFO5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SALESGOODS'


class TjsSalesgoods20210531(models.Model):
    regno = models.IntegerField(db_column='REGNO')  # Field name made lowercase.
    ordercode = models.CharField(db_column='ORDERCODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sdiv = models.CharField(db_column='SDIV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='SCODE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sname = models.CharField(db_column='SNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dno = models.CharField(db_column='DNO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    dname = models.CharField(db_column='DNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wid = models.CharField(db_column='WID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weqname = models.CharField(db_column='WEQNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wdate = models.CharField(db_column='WDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gno = models.IntegerField(db_column='GNO', blank=True, null=True)  # Field name made lowercase.
    gname = models.CharField(db_column='GNAME', max_length=80, blank=True, null=True)  # Field name made lowercase.
    gcnt = models.SmallIntegerField(db_column='GCNT', blank=True, null=True)  # Field name made lowercase.
    gprice = models.IntegerField(db_column='GPRICE', blank=True, null=True)  # Field name made lowercase.
    ginprice = models.IntegerField(db_column='GINPRICE', blank=True, null=True)  # Field name made lowercase.
    pumno = models.CharField(db_column='PUMNO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    appyn = models.CharField(db_column='APPYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dyn = models.CharField(db_column='DYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    psyn = models.CharField(db_column='PSYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    puyn = models.CharField(db_column='PUYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    discntyn = models.CharField(db_column='DISCNTYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    giveyn = models.CharField(db_column='GIVEYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    transyn = models.CharField(db_column='TRANSYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etcyn1 = models.CharField(db_column='ETCYN1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etcyn2 = models.CharField(db_column='ETCYN2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etcyn3 = models.CharField(db_column='ETCYN3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etcyn4 = models.CharField(db_column='ETCYN4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etcyn5 = models.CharField(db_column='ETCYN5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    etcinfo4 = models.CharField(db_column='ETCINFO4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    etcinfo5 = models.CharField(db_column='ETCINFO5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SALESGOODS_20210531'


class TjsSalesvaninfo(models.Model):
    regno = models.IntegerField(db_column='REGNO', blank=True, null=True)  # Field name made lowercase.
    ordercode = models.CharField(db_column='ORDERCODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdiv = models.CharField(db_column='CDIV', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cid = models.CharField(db_column='CID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ceqname = models.CharField(db_column='CEQNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cdate = models.CharField(db_column='CDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    appdate = models.CharField(db_column='APPDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    appno = models.CharField(db_column='APPNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totalcost = models.IntegerField(db_column='TOTALCOST', blank=True, null=True)  # Field name made lowercase.
    vatax = models.IntegerField(db_column='VATAX', blank=True, null=True)  # Field name made lowercase.
    servicefee = models.IntegerField(db_column='SERVICEFEE', blank=True, null=True)  # Field name made lowercase.
    etc1 = models.IntegerField(db_column='ETC1', blank=True, null=True)  # Field name made lowercase.
    etc2 = models.IntegerField(db_column='ETC2', blank=True, null=True)  # Field name made lowercase.
    etc3 = models.IntegerField(db_column='ETC3', blank=True, null=True)  # Field name made lowercase.
    appidinfo = models.CharField(db_column='APPIDINFO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    halboo = models.CharField(db_column='HALBOO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    adminno = models.CharField(db_column='ADMINNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tranno = models.CharField(db_column='TRANNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cpcode = models.SmallIntegerField(db_column='CPCODE', blank=True, null=True)  # Field name made lowercase.
    cregno = models.CharField(db_column='CREGNO', max_length=14, blank=True, null=True)  # Field name made lowercase.
    catid = models.CharField(db_column='CATID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cname1 = models.CharField(db_column='CNAME1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cname2 = models.CharField(db_column='CNAME2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cname3 = models.CharField(db_column='CNAME3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sendstr = models.TextField(db_column='SENDSTR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    recvstr = models.TextField(db_column='RECVSTR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cstate = models.CharField(db_column='CSTATE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SALESVANINFO'


class TjsSales20210531(models.Model):
    ordercode = models.CharField(db_column='ORDERCODE', max_length=20)  # Field name made lowercase.
    appyn = models.CharField(db_column='APPYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cstate = models.CharField(db_column='CSTATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    wtime = models.CharField(db_column='WTIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    stime = models.CharField(db_column='STIME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    refundyn = models.CharField(db_column='REFUNDYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rordercode = models.CharField(db_column='RORDERCODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rdate = models.CharField(db_column='RDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    seqname = models.CharField(db_column='SEQNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wid = models.CharField(db_column='WID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weqname = models.CharField(db_column='WEQNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    wdate = models.CharField(db_column='WDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cpcode = models.SmallIntegerField(db_column='CPCODE', blank=True, null=True)  # Field name made lowercase.
    dno = models.CharField(db_column='DNO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    dname = models.CharField(db_column='DNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mno = models.IntegerField(db_column='MNO', blank=True, null=True)  # Field name made lowercase.
    cno = models.CharField(db_column='CNO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gno = models.CharField(db_column='GNO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    totalcost = models.IntegerField(db_column='TOTALCOST', blank=True, null=True)  # Field name made lowercase.
    finalcost = models.IntegerField(db_column='FINALCOST', blank=True, null=True)  # Field name made lowercase.
    vatax = models.IntegerField(db_column='VATAX', blank=True, null=True)  # Field name made lowercase.
    servicefee = models.IntegerField(db_column='SERVICEFEE', blank=True, null=True)  # Field name made lowercase.
    cash = models.IntegerField(db_column='CASH', blank=True, null=True)  # Field name made lowercase.
    cashr = models.IntegerField(db_column='CASHR', blank=True, null=True)  # Field name made lowercase.
    card = models.IntegerField(db_column='CARD', blank=True, null=True)  # Field name made lowercase.
    cardm = models.IntegerField(db_column='CARDM', blank=True, null=True)  # Field name made lowercase.
    mcharge = models.IntegerField(db_column='MCHARGE', blank=True, null=True)  # Field name made lowercase.
    mpoint = models.IntegerField(db_column='MPOINT', blank=True, null=True)  # Field name made lowercase.
    giftcard = models.IntegerField(db_column='GIFTCARD', blank=True, null=True)  # Field name made lowercase.
    misoo = models.IntegerField(db_column='MISOO', blank=True, null=True)  # Field name made lowercase.
    misooinfo = models.CharField(db_column='MISOOINFO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ocost1 = models.IntegerField(db_column='OCOST1', blank=True, null=True)  # Field name made lowercase.
    ocost2 = models.IntegerField(db_column='OCOST2', blank=True, null=True)  # Field name made lowercase.
    ocost3 = models.IntegerField(db_column='OCOST3', blank=True, null=True)  # Field name made lowercase.
    ocost4 = models.IntegerField(db_column='OCOST4', blank=True, null=True)  # Field name made lowercase.
    ocost5 = models.IntegerField(db_column='OCOST5', blank=True, null=True)  # Field name made lowercase.
    ocost6 = models.IntegerField(db_column='OCOST6', blank=True, null=True)  # Field name made lowercase.
    ocost7 = models.IntegerField(db_column='OCOST7', blank=True, null=True)  # Field name made lowercase.
    ocost8 = models.IntegerField(db_column='OCOST8', blank=True, null=True)  # Field name made lowercase.
    opoint1 = models.IntegerField(db_column='OPOINT1', blank=True, null=True)  # Field name made lowercase.
    opoint2 = models.IntegerField(db_column='OPOINT2', blank=True, null=True)  # Field name made lowercase.
    opoint3 = models.IntegerField(db_column='OPOINT3', blank=True, null=True)  # Field name made lowercase.
    opoint4 = models.IntegerField(db_column='OPOINT4', blank=True, null=True)  # Field name made lowercase.
    opoint5 = models.IntegerField(db_column='OPOINT5', blank=True, null=True)  # Field name made lowercase.
    opoint6 = models.IntegerField(db_column='OPOINT6', blank=True, null=True)  # Field name made lowercase.
    opoint7 = models.IntegerField(db_column='OPOINT7', blank=True, null=True)  # Field name made lowercase.
    opoint8 = models.IntegerField(db_column='OPOINT8', blank=True, null=True)  # Field name made lowercase.
    discnt1 = models.CharField(db_column='DISCNT1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    discntinfo1 = models.CharField(db_column='DISCNTINFO1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt2 = models.CharField(db_column='DISCNT2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo2 = models.CharField(db_column='DISCNTINFO2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt3 = models.CharField(db_column='DISCNT3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo3 = models.CharField(db_column='DISCNTINFO3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt4 = models.CharField(db_column='DISCNT4', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo4 = models.CharField(db_column='DISCNTINFO4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt5 = models.CharField(db_column='DISCNT5', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo5 = models.CharField(db_column='DISCNTINFO5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt6 = models.CharField(db_column='DISCNT6', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo6 = models.CharField(db_column='DISCNTINFO6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt7 = models.CharField(db_column='DISCNT7', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo7 = models.CharField(db_column='DISCNTINFO7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    discnt8 = models.CharField(db_column='DISCNT8', max_length=15, blank=True, null=True)  # Field name made lowercase.
    discntinfo8 = models.CharField(db_column='DISCNTINFO8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    smemo = models.CharField(db_column='SMEMO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SALES_20210531'


class TjsSalesxcorp(models.Model):
    cpcode = models.CharField(db_column='CPCODE', max_length=10)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=10)  # Field name made lowercase.
    yno = models.SmallIntegerField(db_column='YNO', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.IntegerField(db_column='TOTALCOST', blank=True, null=True)  # Field name made lowercase.
    finalcost = models.IntegerField(db_column='FINALCOST', blank=True, null=True)  # Field name made lowercase.
    vatax = models.IntegerField(db_column='VATAX', blank=True, null=True)  # Field name made lowercase.
    servicefee = models.IntegerField(db_column='SERVICEFEE', blank=True, null=True)  # Field name made lowercase.
    cash = models.IntegerField(db_column='CASH', blank=True, null=True)  # Field name made lowercase.
    cashr = models.IntegerField(db_column='CASHR', blank=True, null=True)  # Field name made lowercase.
    card = models.IntegerField(db_column='CARD', blank=True, null=True)  # Field name made lowercase.
    cardm = models.IntegerField(db_column='CARDM', blank=True, null=True)  # Field name made lowercase.
    mcharge = models.IntegerField(db_column='MCHARGE', blank=True, null=True)  # Field name made lowercase.
    mpoint = models.IntegerField(db_column='MPOINT', blank=True, null=True)  # Field name made lowercase.
    giftcard = models.IntegerField(db_column='GIFTCARD', blank=True, null=True)  # Field name made lowercase.
    ocost1 = models.IntegerField(db_column='OCOST1', blank=True, null=True)  # Field name made lowercase.
    ocost2 = models.IntegerField(db_column='OCOST2', blank=True, null=True)  # Field name made lowercase.
    ocost3 = models.IntegerField(db_column='OCOST3', blank=True, null=True)  # Field name made lowercase.
    ocost4 = models.IntegerField(db_column='OCOST4', blank=True, null=True)  # Field name made lowercase.
    ocost5 = models.IntegerField(db_column='OCOST5', blank=True, null=True)  # Field name made lowercase.
    ocost6 = models.IntegerField(db_column='OCOST6', blank=True, null=True)  # Field name made lowercase.
    ocost7 = models.IntegerField(db_column='OCOST7', blank=True, null=True)  # Field name made lowercase.
    ocost8 = models.IntegerField(db_column='OCOST8', blank=True, null=True)  # Field name made lowercase.
    opoint1 = models.IntegerField(db_column='OPOINT1', blank=True, null=True)  # Field name made lowercase.
    opoint2 = models.IntegerField(db_column='OPOINT2', blank=True, null=True)  # Field name made lowercase.
    opoint3 = models.IntegerField(db_column='OPOINT3', blank=True, null=True)  # Field name made lowercase.
    opoint4 = models.IntegerField(db_column='OPOINT4', blank=True, null=True)  # Field name made lowercase.
    opoint5 = models.IntegerField(db_column='OPOINT5', blank=True, null=True)  # Field name made lowercase.
    opoint6 = models.IntegerField(db_column='OPOINT6', blank=True, null=True)  # Field name made lowercase.
    opoint7 = models.IntegerField(db_column='OPOINT7', blank=True, null=True)  # Field name made lowercase.
    opoint8 = models.IntegerField(db_column='OPOINT8', blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gcash = models.IntegerField(db_column='GCASH', blank=True, null=True)  # Field name made lowercase.
    gcard = models.IntegerField(db_column='GCARD', blank=True, null=True)  # Field name made lowercase.
    getc = models.IntegerField(db_column='GETC', blank=True, null=True)  # Field name made lowercase.
    bcharge = models.IntegerField(db_column='BCHARGE', blank=True, null=True)  # Field name made lowercase.
    tcharge = models.IntegerField(db_column='TCHARGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SALESxCORP'


class TjsSalesxcorpxd(models.Model):
    cpcode = models.CharField(db_column='CPCODE', max_length=10)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=10)  # Field name made lowercase.
    dno = models.CharField(db_column='DNO', max_length=10)  # Field name made lowercase.
    dname = models.CharField(db_column='DNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    yno = models.SmallIntegerField(db_column='YNO', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.IntegerField(db_column='TOTALCOST', blank=True, null=True)  # Field name made lowercase.
    finalcost = models.IntegerField(db_column='FINALCOST', blank=True, null=True)  # Field name made lowercase.
    vatax = models.IntegerField(db_column='VATAX', blank=True, null=True)  # Field name made lowercase.
    servicefee = models.IntegerField(db_column='SERVICEFEE', blank=True, null=True)  # Field name made lowercase.
    cash = models.IntegerField(db_column='CASH', blank=True, null=True)  # Field name made lowercase.
    cashr = models.IntegerField(db_column='CASHR', blank=True, null=True)  # Field name made lowercase.
    card = models.IntegerField(db_column='CARD', blank=True, null=True)  # Field name made lowercase.
    cardm = models.IntegerField(db_column='CARDM', blank=True, null=True)  # Field name made lowercase.
    mcharge = models.IntegerField(db_column='MCHARGE', blank=True, null=True)  # Field name made lowercase.
    mpoint = models.IntegerField(db_column='MPOINT', blank=True, null=True)  # Field name made lowercase.
    giftcard = models.IntegerField(db_column='GIFTCARD', blank=True, null=True)  # Field name made lowercase.
    ocost1 = models.IntegerField(db_column='OCOST1', blank=True, null=True)  # Field name made lowercase.
    ocost2 = models.IntegerField(db_column='OCOST2', blank=True, null=True)  # Field name made lowercase.
    ocost3 = models.IntegerField(db_column='OCOST3', blank=True, null=True)  # Field name made lowercase.
    ocost4 = models.IntegerField(db_column='OCOST4', blank=True, null=True)  # Field name made lowercase.
    ocost5 = models.IntegerField(db_column='OCOST5', blank=True, null=True)  # Field name made lowercase.
    ocost6 = models.IntegerField(db_column='OCOST6', blank=True, null=True)  # Field name made lowercase.
    ocost7 = models.IntegerField(db_column='OCOST7', blank=True, null=True)  # Field name made lowercase.
    ocost8 = models.IntegerField(db_column='OCOST8', blank=True, null=True)  # Field name made lowercase.
    opoint1 = models.IntegerField(db_column='OPOINT1', blank=True, null=True)  # Field name made lowercase.
    opoint2 = models.IntegerField(db_column='OPOINT2', blank=True, null=True)  # Field name made lowercase.
    opoint3 = models.IntegerField(db_column='OPOINT3', blank=True, null=True)  # Field name made lowercase.
    opoint4 = models.IntegerField(db_column='OPOINT4', blank=True, null=True)  # Field name made lowercase.
    opoint5 = models.IntegerField(db_column='OPOINT5', blank=True, null=True)  # Field name made lowercase.
    opoint6 = models.IntegerField(db_column='OPOINT6', blank=True, null=True)  # Field name made lowercase.
    opoint7 = models.IntegerField(db_column='OPOINT7', blank=True, null=True)  # Field name made lowercase.
    opoint8 = models.IntegerField(db_column='OPOINT8', blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gcash = models.IntegerField(db_column='GCASH', blank=True, null=True)  # Field name made lowercase.
    gcard = models.IntegerField(db_column='GCARD', blank=True, null=True)  # Field name made lowercase.
    getc = models.IntegerField(db_column='GETC', blank=True, null=True)  # Field name made lowercase.
    bcharge = models.IntegerField(db_column='BCHARGE', blank=True, null=True)  # Field name made lowercase.
    tcharge = models.IntegerField(db_column='TCHARGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SALESxCORPxD'


class TjsSalesxjumpan(models.Model):
    cpcode = models.CharField(db_column='CPCODE', max_length=10)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=10)  # Field name made lowercase.
    scode = models.CharField(db_column='SCODE', max_length=10)  # Field name made lowercase.
    yno = models.SmallIntegerField(db_column='YNO', blank=True, null=True)  # Field name made lowercase.
    tcnt = models.IntegerField(db_column='TCNT', blank=True, null=True)  # Field name made lowercase.
    tcost = models.IntegerField(db_column='TCOST', blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tcash = models.IntegerField(db_column='TCASH', blank=True, null=True)  # Field name made lowercase.
    tcard = models.IntegerField(db_column='TCARD', blank=True, null=True)  # Field name made lowercase.
    tcashr = models.IntegerField(db_column='TCASHR', blank=True, null=True)  # Field name made lowercase.
    tcardm = models.IntegerField(db_column='TCARDM', blank=True, null=True)  # Field name made lowercase.
    tmcharge = models.IntegerField(db_column='TMCHARGE', blank=True, null=True)  # Field name made lowercase.
    tocost1 = models.IntegerField(db_column='TOCOST1', blank=True, null=True)  # Field name made lowercase.
    tocost2 = models.IntegerField(db_column='TOCOST2', blank=True, null=True)  # Field name made lowercase.
    tocost3 = models.IntegerField(db_column='TOCOST3', blank=True, null=True)  # Field name made lowercase.
    tocost4 = models.IntegerField(db_column='TOCOST4', blank=True, null=True)  # Field name made lowercase.
    tocost5 = models.IntegerField(db_column='TOCOST5', blank=True, null=True)  # Field name made lowercase.
    tocost6 = models.IntegerField(db_column='TOCOST6', blank=True, null=True)  # Field name made lowercase.
    tocost7 = models.IntegerField(db_column='TOCOST7', blank=True, null=True)  # Field name made lowercase.
    tocost8 = models.IntegerField(db_column='TOCOST8', blank=True, null=True)  # Field name made lowercase.
    dcash = models.IntegerField(db_column='DCASH', blank=True, null=True)  # Field name made lowercase.
    dcard = models.IntegerField(db_column='DCARD', blank=True, null=True)  # Field name made lowercase.
    jcash = models.IntegerField(db_column='JCASH', blank=True, null=True)  # Field name made lowercase.
    jcard = models.IntegerField(db_column='JCARD', blank=True, null=True)  # Field name made lowercase.
    scash = models.IntegerField(db_column='SCASH', blank=True, null=True)  # Field name made lowercase.
    scard = models.IntegerField(db_column='SCARD', blank=True, null=True)  # Field name made lowercase.
    tricost = models.IntegerField(db_column='TRICOST', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SALESxJUMPAN'


class TjsSalesxmember(models.Model):
    cpcode = models.CharField(db_column='CPCODE', max_length=10)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=10)  # Field name made lowercase.
    yno = models.SmallIntegerField(db_column='YNO', blank=True, null=True)  # Field name made lowercase.
    acnt = models.IntegerField(db_column='ACNT', blank=True, null=True)  # Field name made lowercase.
    aprice = models.IntegerField(db_column='APRICE', blank=True, null=True)  # Field name made lowercase.
    bcnt = models.IntegerField(db_column='BCNT', blank=True, null=True)  # Field name made lowercase.
    bprice = models.IntegerField(db_column='BPRICE', blank=True, null=True)  # Field name made lowercase.
    ccnt = models.IntegerField(db_column='CCNT', blank=True, null=True)  # Field name made lowercase.
    cprice = models.IntegerField(db_column='CPRICE', blank=True, null=True)  # Field name made lowercase.
    dcnt = models.IntegerField(db_column='DCNT', blank=True, null=True)  # Field name made lowercase.
    dprice = models.IntegerField(db_column='DPRICE', blank=True, null=True)  # Field name made lowercase.
    ecnt = models.IntegerField(db_column='ECNT', blank=True, null=True)  # Field name made lowercase.
    eprice = models.IntegerField(db_column='EPRICE', blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SALESxMEMBER'


class TjsSalesxmemberxd(models.Model):
    cpcode = models.CharField(db_column='CPCODE', max_length=10)  # Field name made lowercase.
    sdate = models.CharField(db_column='SDATE', max_length=10)  # Field name made lowercase.
    dno = models.CharField(db_column='DNO', max_length=10)  # Field name made lowercase.
    dname = models.CharField(db_column='DNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    yno = models.SmallIntegerField(db_column='YNO', blank=True, null=True)  # Field name made lowercase.
    acnt = models.IntegerField(db_column='ACNT', blank=True, null=True)  # Field name made lowercase.
    aprice = models.IntegerField(db_column='APRICE', blank=True, null=True)  # Field name made lowercase.
    bcnt = models.IntegerField(db_column='BCNT', blank=True, null=True)  # Field name made lowercase.
    bprice = models.IntegerField(db_column='BPRICE', blank=True, null=True)  # Field name made lowercase.
    ccnt = models.IntegerField(db_column='CCNT', blank=True, null=True)  # Field name made lowercase.
    cprice = models.IntegerField(db_column='CPRICE', blank=True, null=True)  # Field name made lowercase.
    dcnt = models.IntegerField(db_column='DCNT', blank=True, null=True)  # Field name made lowercase.
    dprice = models.IntegerField(db_column='DPRICE', blank=True, null=True)  # Field name made lowercase.
    ecnt = models.IntegerField(db_column='ECNT', blank=True, null=True)  # Field name made lowercase.
    eprice = models.IntegerField(db_column='EPRICE', blank=True, null=True)  # Field name made lowercase.
    etcinfo1 = models.CharField(db_column='ETCINFO1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    etcinfo2 = models.CharField(db_column='ETCINFO2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etcinfo3 = models.CharField(db_column='ETCINFO3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SALESxMEMBERxD'


class TjsSaleBox(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    salebox_cd = models.CharField(db_column='SALEBOX_CD', max_length=20)  # Field name made lowercase.
    salebox_nm = models.CharField(db_column='SALEBOX_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SALE_BOX'
        unique_together = (('shop_cd', 'salebox_cd'),)


class TjsScheduleTaskMng(models.Model):
    task_id = models.CharField(db_column='TASK_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    service_div = models.CharField(db_column='SERVICE_DIV', max_length=100, blank=True, null=True)  # Field name made lowercase.
    task_status_cd = models.CharField(db_column='TASK_STATUS_CD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    task_start_dtm = models.DateTimeField(db_column='TASK_START_DTM', blank=True, null=True)  # Field name made lowercase.
    task_end_dtm = models.DateTimeField(db_column='TASK_END_DTM', blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SCHEDULE_TASK_MNG'


class TjsSetequipment(models.Model):
    div = models.CharField(db_column='DIV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='CLASS', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    info = models.CharField(db_column='INFO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    eqcode = models.CharField(db_column='EQCODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    set1 = models.CharField(db_column='SET1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set2 = models.CharField(db_column='SET2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set3 = models.CharField(db_column='SET3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set4 = models.CharField(db_column='SET4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set5 = models.CharField(db_column='SET5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set6 = models.CharField(db_column='SET6', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set7 = models.CharField(db_column='SET7', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set8 = models.CharField(db_column='SET8', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set9 = models.CharField(db_column='SET9', max_length=700, blank=True, null=True)  # Field name made lowercase.
    set10 = models.CharField(db_column='SET10', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regid = models.CharField(db_column='REGID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    adjid = models.CharField(db_column='ADJID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adjdate = models.CharField(db_column='ADJDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SETEQUIPMENT'


class TjsShop(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=40)  # Field name made lowercase.
    shop_nm = models.CharField(db_column='SHOP_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    biz_no = models.CharField(db_column='BIZ_NO', max_length=14, blank=True, null=True)  # Field name made lowercase.
    rprsn_nm = models.CharField(db_column='RPRSN_NM', max_length=80, blank=True, null=True)  # Field name made lowercase.
    acct_no = models.CharField(db_column='ACCT_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tel_no = models.CharField(db_column='TEL_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sms_snd_tel_no = models.CharField(db_column='SMS_SND_TEL_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bk_cd = models.CharField(db_column='BK_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    bk_nm = models.CharField(db_column='BK_NM', max_length=80, blank=True, null=True)  # Field name made lowercase.
    hgrk_dpt_nm = models.CharField(db_column='HGRK_DPT_NM', max_length=80, blank=True, null=True)  # Field name made lowercase.
    zip_cd = models.CharField(db_column='ZIP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    adr = models.CharField(db_column='ADR', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fax_no = models.CharField(db_column='FAX_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dvc_no = models.CharField(db_column='DVC_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    plus_frnd_id = models.CharField(db_column='PLUS_FRND_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    alim_talk_snd_key = models.CharField(db_column='ALIM_TALK_SND_KEY', max_length=40, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SHOP'


class TjsShopChngHis(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=40)  # Field name made lowercase.
    shop_nm_bf = models.CharField(db_column='SHOP_NM_BF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    shop_nm_af = models.CharField(db_column='SHOP_NM_AF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    biz_no_bf = models.CharField(db_column='BIZ_NO_BF', max_length=14, blank=True, null=True)  # Field name made lowercase.
    biz_no_af = models.CharField(db_column='BIZ_NO_AF', max_length=14, blank=True, null=True)  # Field name made lowercase.
    rprsn_nm_bf = models.CharField(db_column='RPRSN_NM_BF', max_length=80, blank=True, null=True)  # Field name made lowercase.
    rprsn_nm_af = models.CharField(db_column='RPRSN_NM_AF', max_length=80, blank=True, null=True)  # Field name made lowercase.
    acct_no_bf = models.CharField(db_column='ACCT_NO_BF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    acct_no_af = models.CharField(db_column='ACCT_NO_AF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tel_no_bf = models.CharField(db_column='TEL_NO_BF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tel_no_af = models.CharField(db_column='TEL_NO_AF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bk_cd_bf = models.CharField(db_column='BK_CD_BF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    bk_cd_af = models.CharField(db_column='BK_CD_AF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    bk_nm_bf = models.CharField(db_column='BK_NM_BF', max_length=80, blank=True, null=True)  # Field name made lowercase.
    bk_nm_af = models.CharField(db_column='BK_NM_AF', max_length=80, blank=True, null=True)  # Field name made lowercase.
    hgrk_dpt_nm_bf = models.CharField(db_column='HGRK_DPT_NM_BF', max_length=80, blank=True, null=True)  # Field name made lowercase.
    hgrk_dpt_nm_af = models.CharField(db_column='HGRK_DPT_NM_AF', max_length=80, blank=True, null=True)  # Field name made lowercase.
    dvc_no_bf = models.CharField(db_column='DVC_NO_BF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dvc_no_af = models.CharField(db_column='DVC_NO_AF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    chng_cd = models.CharField(db_column='CHNG_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SHOP_CHNG_HIS'


class TjsShopTmp(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=40)  # Field name made lowercase.
    shop_nm = models.CharField(db_column='SHOP_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    biz_no = models.CharField(db_column='BIZ_NO', max_length=14, blank=True, null=True)  # Field name made lowercase.
    rprsn_nm = models.CharField(db_column='RPRSN_NM', max_length=80, blank=True, null=True)  # Field name made lowercase.
    acct_no = models.CharField(db_column='ACCT_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tel_no = models.CharField(db_column='TEL_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bk_cd = models.CharField(db_column='BK_CD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    bk_nm = models.CharField(db_column='BK_NM', max_length=80, blank=True, null=True)  # Field name made lowercase.
    hgrk_dpt_nm = models.CharField(db_column='HGRK_DPT_NM', max_length=80, blank=True, null=True)  # Field name made lowercase.
    dvc_no = models.CharField(db_column='DVC_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    zip_cd = models.CharField(db_column='ZIP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    adr = models.CharField(db_column='ADR', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fax_no = models.CharField(db_column='FAX_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SHOP_TMP'


class TjsSlipCountH(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    module_cd = models.CharField(db_column='MODULE_CD', max_length=6)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=5, decimal_places=0)  # Field name made lowercase.
    prefix_cd = models.CharField(db_column='PREFIX_CD', max_length=6)  # Field name made lowercase.
    prefix_nm = models.CharField(db_column='PREFIX_NM', max_length=100)  # Field name made lowercase.
    cnt_cd = models.CharField(db_column='CNT_CD', max_length=6)  # Field name made lowercase.
    serial_qt = models.DecimalField(db_column='SERIAL_QT', max_digits=5, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SLIP_COUNT_H'
        unique_together = (('shop_cd', 'module_cd', 'line_no'),)


class TjsSlipCountL(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    module_cd = models.CharField(db_column='MODULE_CD', max_length=6)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=5, decimal_places=0)  # Field name made lowercase.
    cnt_cd = models.CharField(db_column='CNT_CD', max_length=10)  # Field name made lowercase.
    prefix_cd = models.CharField(db_column='PREFIX_CD', max_length=6)  # Field name made lowercase.
    serial_no = models.CharField(db_column='SERIAL_NO', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SLIP_COUNT_L'
        unique_together = (('shop_cd', 'module_cd', 'line_no', 'cnt_cd', 'prefix_cd'),)


class TjsSmsConfigH(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    sms_cd = models.CharField(db_column='SMS_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sms_nm = models.CharField(db_column='SMS_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sms_tp = models.CharField(db_column='SMS_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    detail_dc = models.CharField(db_column='DETAIL_DC', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    sms_yn = models.CharField(db_column='SMS_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    talk_yn = models.CharField(db_column='TALK_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SMS_CONFIG_H'
        unique_together = (('shop_cd', 'line_no'),)


class TjsSmsForm(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contents = models.CharField(db_column='CONTENTS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ad_yn = models.CharField(db_column='AD_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    term_yn = models.CharField(db_column='TERM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    indv_nm_yn = models.CharField(db_column='INDV_NM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SMS_FORM'
        unique_together = (('shop_cd', 'line_no'),)


class TjsSmsH(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    slip_no = models.CharField(db_column='SLIP_NO', max_length=40)  # Field name made lowercase.
    sms_dt = models.CharField(db_column='SMS_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    rsrv_yn = models.CharField(db_column='RSRV_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rsrv_dtm = models.CharField(db_column='RSRV_DTM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ad_yn = models.CharField(db_column='AD_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    term_yn = models.CharField(db_column='TERM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    indv_nm_yn = models.CharField(db_column='INDV_NM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SMS_H'
        unique_together = (('shop_cd', 'slip_no'),)


class TjsSmsL(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    slip_no = models.CharField(db_column='SLIP_NO', max_length=40)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tel_no = models.CharField(db_column='TEL_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    contents = models.CharField(db_column='CONTENTS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SMS_L'
        unique_together = (('shop_cd', 'slip_no', 'line_no'),)


class TjsSmsSend(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    snd_dtm = models.DateTimeField(db_column='SND_DTM', blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tel = models.CharField(db_column='CUST_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contents = models.CharField(db_column='CONTENTS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rsrv_yn = models.CharField(db_column='RSRV_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ad_yn = models.CharField(db_column='AD_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    term_yn = models.CharField(db_column='TERM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    indv_nm_yn = models.CharField(db_column='INDV_NM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_SMS_SEND'
        unique_together = (('shop_cd', 'line_no'),)


class TjsTimeMas(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    time = models.CharField(db_column='TIME', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_TIME_MAS'


class TjsVanCntTmp(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    pay_dt = models.CharField(db_column='PAY_DT', max_length=8)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=20)  # Field name made lowercase.
    van_cnt = models.DecimalField(db_column='VAN_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pan_cnt = models.DecimalField(db_column='PAN_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_VAN_CNT_TMP'
        unique_together = (('shop_cd', 'pay_dt', 'pay_no'),)


class TjsVanCode(models.Model):
    rcv_cd = models.CharField(db_column='RCV_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    msg_kr = models.CharField(db_column='MSG_KR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    msg_en = models.CharField(db_column='MSG_EN', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_VAN_CODE'


class TjsVanHst(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slip_no = models.CharField(db_column='SLIP_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    card_div_cd = models.CharField(db_column='CARD_DIV_CD', max_length=6, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    eq_cd = models.CharField(db_column='EQ_CD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    card_dt = models.DateTimeField(db_column='CARD_DT', blank=True, null=True)  # Field name made lowercase.
    app_id_info = models.CharField(db_column='APP_ID_INFO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cat_id = models.CharField(db_column='CAT_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    snd_str = models.CharField(db_column='SND_STR', max_length=4000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_VAN_HST'


class TjsVanInfo(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    slip_no = models.CharField(db_column='SLIP_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    card_div_cd = models.CharField(db_column='CARD_DIV_CD', max_length=6, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    eq_cd = models.CharField(db_column='EQ_CD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    card_dt = models.DateTimeField(db_column='CARD_DT', blank=True, null=True)  # Field name made lowercase.
    app_dt = models.CharField(db_column='APP_DT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    app_no = models.CharField(db_column='APP_NO', max_length=14, blank=True, null=True)  # Field name made lowercase.
    total_cost = models.DecimalField(db_column='TOTAL_COST', max_digits=17, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    vat_cost = models.DecimalField(db_column='VAT_COST', max_digits=17, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    service_cost = models.DecimalField(db_column='SERVICE_COST', max_digits=17, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    app_id_info = models.CharField(db_column='APP_ID_INFO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    instl_month = models.CharField(db_column='INSTL_MONTH', max_length=4, blank=True, null=True)  # Field name made lowercase.
    admin_no = models.CharField(db_column='ADMIN_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    trn_no = models.CharField(db_column='TRN_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    biz_no = models.CharField(db_column='BIZ_NO', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cat_id = models.CharField(db_column='CAT_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    card_nm1 = models.CharField(db_column='CARD_NM1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    card_nm2 = models.CharField(db_column='CARD_NM2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    card_nm3 = models.CharField(db_column='CARD_NM3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    snd_str = models.CharField(db_column='SND_STR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    rcv_str = models.CharField(db_column='RCV_STR', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    stat_cd = models.CharField(db_column='STAT_CD', max_length=14, blank=True, null=True)  # Field name made lowercase.
    etc1 = models.CharField(db_column='ETC1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc2 = models.CharField(db_column='ETC2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc3 = models.CharField(db_column='ETC3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJS_VAN_INFO'


class TjuStaffidinfo(models.Model):
    scode = models.CharField(db_column='SCODE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=30)  # Field name made lowercase.
    spw = models.CharField(db_column='SPW', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usecode = models.SmallIntegerField(db_column='USECODE', blank=True, null=True)  # Field name made lowercase.
    set1 = models.CharField(db_column='SET1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    set2 = models.CharField(db_column='SET2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set3 = models.IntegerField(db_column='SET3', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    appyn = models.CharField(db_column='APPYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    regid = models.CharField(db_column='REGID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    adjid = models.CharField(db_column='ADJID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adjdate = models.CharField(db_column='ADJDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJU_STAFFIDINFO'


class TjwCustAnlyGrpDtl(models.Model):
    anly_grp_dtl_id = models.CharField(db_column='ANLY_GRP_DTL_ID', max_length=20)  # Field name made lowercase.
    anly_grp_id = models.CharField(db_column='ANLY_GRP_ID', max_length=20)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ')  # Field name made lowercase.
    op_main = models.CharField(db_column='OP_MAIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    op_sub = models.CharField(db_column='OP_SUB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    conj = models.CharField(db_column='CONJ', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJW_CUST_ANLY_GRP_DTL'


class TjwCustAnlyGrpMng(models.Model):
    anly_grp_id = models.CharField(db_column='ANLY_GRP_ID', max_length=20)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=20)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ')  # Field name made lowercase.
    anly_grp_nm = models.CharField(db_column='ANLY_GRP_NM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    disp_yn = models.CharField(db_column='DISP_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJW_CUST_ANLY_GRP_MNG'


class TjwMenu(models.Model):
    menu_id = models.IntegerField(db_column='MENU_ID', primary_key=True)  # Field name made lowercase.
    parent_menu_id = models.IntegerField(db_column='PARENT_MENU_ID')  # Field name made lowercase.
    menu_nm = models.CharField(db_column='MENU_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    link_url = models.CharField(db_column='LINK_URL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    depth = models.IntegerField(db_column='DEPTH', blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.IntegerField(db_column='SORT_SEQ', blank=True, null=True)  # Field name made lowercase.
    dsc = models.CharField(db_column='DSC', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    auth_use_yn = models.CharField(db_column='AUTH_USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJW_MENU'


class TjwMenuUsrAuth(models.Model):
    menu_id = models.IntegerField(db_column='MENU_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=50)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJW_MENU_USR_AUTH'
        unique_together = (('menu_id', 'user_id'),)


class TjwMenuUsrGrpAuth(models.Model):
    menu_id = models.IntegerField(db_column='MENU_ID', primary_key=True)  # Field name made lowercase.
    user_grp_cd = models.IntegerField(db_column='USER_GRP_CD')  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJW_MENU_USR_GRP_AUTH'
        unique_together = (('menu_id', 'user_grp_cd'),)


class TjwPerformTargetMng(models.Model):
    term_div_cd = models.CharField(db_column='TERM_DIV_CD', max_length=1)  # Field name made lowercase.
    perform_div_cd = models.CharField(db_column='PERFORM_DIV_CD', max_length=2)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20)  # Field name made lowercase.
    year = models.CharField(db_column='YEAR', max_length=4, blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(db_column='MONTH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    week = models.CharField(db_column='WEEK', max_length=1, blank=True, null=True)  # Field name made lowercase.
    target = models.DecimalField(db_column='TARGET', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TJW_PERFORM_TARGET_MNG'


class ZmigTjsCustDesigner(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    main_yn = models.CharField(db_column='MAIN_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_CUST_DESIGNER'


class ZmigTjsCustInfo(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_card_no = models.CharField(db_column='CUST_CARD_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender_cd = models.CharField(db_column='GENDER_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lv_cd = models.CharField(db_column='LV_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birth_dt = models.CharField(db_column='BIRTH_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    birth_div = models.CharField(db_column='BIRTH_DIV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cp_tel = models.CharField(db_column='CP_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zip_cd = models.CharField(db_column='ZIP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    adr = models.CharField(db_column='ADR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    adr_dtl = models.CharField(db_column='ADR_DTL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    marry_yn = models.CharField(db_column='MARRY_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nation_cd = models.CharField(db_column='NATION_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vst_rt_cd = models.CharField(db_column='VST_RT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    frst_vst_dt = models.CharField(db_column='FRST_VST_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lst_vst_dt = models.CharField(db_column='LST_VST_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    anniv_dt = models.CharField(db_column='ANNIV_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sms_yn = models.CharField(db_column='SMS_YN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vst_cnt = models.DecimalField(db_column='VST_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcmd_cnt = models.DecimalField(db_column='RCMD_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    car_no = models.CharField(db_column='CAR_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    drink_inf = models.CharField(db_column='DRINK_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shmp_tch_inf = models.CharField(db_column='SHMP_TCH_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shmp_inf = models.CharField(db_column='SHMP_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tip_inf = models.CharField(db_column='TIP_INF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taste_1 = models.CharField(db_column='TASTE_1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taste_2 = models.CharField(db_column='TASTE_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fam_cd = models.CharField(db_column='FAM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    warn_yn = models.CharField(db_column='WARN_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    anniv_tp = models.CharField(db_column='ANNIV_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    birth_yy = models.CharField(db_column='BIRTH_YY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    birth_md = models.CharField(db_column='BIRTH_MD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    inactive_yn = models.CharField(db_column='INACTIVE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fnl_shop_cd = models.CharField(db_column='FNL_SHOP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_CUST_INFO'


class ZmigTjsCustInfoSum(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=10)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prpd_new_amt = models.DecimalField(db_column='PRPD_NEW_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ticket_cnt = models.DecimalField(db_column='TICKET_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pay_tot_amt = models.DecimalField(db_column='PAY_TOT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vst_cnt = models.DecimalField(db_column='VST_CNT', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    prpd_rt = models.DecimalField(db_column='PRPD_RT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_CUST_INFO_SUM'


class ZmigTjsCustMemo(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo_color = models.CharField(db_column='MEMO_COLOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    warn_yn = models.CharField(db_column='WARN_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.
    memo_tp = models.CharField(db_column='MEMO_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_CUST_MEMO'


class ZmigTjsCustPrepaidList(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=5, decimal_places=0)  # Field name made lowercase.
    io_fg = models.CharField(db_column='IO_FG', max_length=10)  # Field name made lowercase.
    prpd_cd = models.CharField(db_column='PRPD_CD', max_length=10)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_cust_cd = models.CharField(db_column='RCV_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_dsgn_cd = models.CharField(db_column='RCV_DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    use_div_cd = models.CharField(db_column='USE_DIV_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_CUST_PREPAID_LIST'


class ZmigTjsCustPrepaidMove(models.Model):
    trns_no = models.CharField(db_column='TRNS_NO', max_length=40)  # Field name made lowercase.
    trns_tp = models.CharField(db_column='TRNS_TP', max_length=10)  # Field name made lowercase.
    snd_cust_cd = models.CharField(db_column='SND_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_cust_cd = models.CharField(db_column='RCV_CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    snd_dno_cd = models.CharField(db_column='SND_DNO_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rcv_dno_cd = models.CharField(db_column='RCV_DNO_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prpd_amt = models.DecimalField(db_column='PRPD_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_CUST_PREPAID_MOVE'


class ZmigTjsCustTicket(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    start_dt = models.CharField(db_column='START_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    end_dt = models.CharField(db_column='END_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    org_cnt = models.DecimalField(db_column='ORG_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    use_cnt = models.DecimalField(db_column='USE_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    res_cnt = models.DecimalField(db_column='RES_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_CUST_TICKET'


class ZmigTjsCustTicketList(models.Model):
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    use_dtm = models.DateTimeField(db_column='USE_DTM', blank=True, null=True)  # Field name made lowercase.
    use_cnt = models.DecimalField(db_column='USE_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_CUST_TICKET_LIST'


class ZmigTjsEquipment(models.Model):
    eqcode = models.IntegerField(db_column='EQCODE')  # Field name made lowercase.
    cpcode = models.SmallIntegerField(db_column='CPCODE', blank=True, null=True)  # Field name made lowercase.
    eqname = models.CharField(db_column='EQNAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    macid = models.CharField(db_column='MACID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ediv = models.CharField(db_column='EDIV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etc1 = models.CharField(db_column='ETC1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc2 = models.CharField(db_column='ETC2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc3 = models.CharField(db_column='ETC3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc4 = models.CharField(db_column='ETC4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc5 = models.CharField(db_column='ETC5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc6 = models.CharField(db_column='ETC6', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc7 = models.CharField(db_column='ETC7', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc8 = models.CharField(db_column='ETC8', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc9 = models.CharField(db_column='ETC9', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc10 = models.CharField(db_column='ETC10', max_length=30, blank=True, null=True)  # Field name made lowercase.
    appyn = models.CharField(db_column='APPYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    regid = models.CharField(db_column='REGID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    adjid = models.CharField(db_column='ADJID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adjdate = models.CharField(db_column='ADJDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_EQUIPMENT'


class ZmigTjsEquipmentsub(models.Model):
    eqcode = models.IntegerField(db_column='EQCODE')  # Field name made lowercase.
    ediv = models.CharField(db_column='EDIV', max_length=2)  # Field name made lowercase.
    einfo = models.CharField(db_column='EINFO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    useyn = models.CharField(db_column='USEYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    usestr = models.CharField(db_column='USESTR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    itface = models.CharField(db_column='ITFACE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    speed = models.CharField(db_column='SPEED', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rtime = models.IntegerField(db_column='RTIME', blank=True, null=True)  # Field name made lowercase.
    setdate = models.CharField(db_column='SETDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc1 = models.CharField(db_column='ETC1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc2 = models.CharField(db_column='ETC2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc3 = models.CharField(db_column='ETC3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regid = models.CharField(db_column='REGID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    adjid = models.CharField(db_column='ADJID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adjdate = models.CharField(db_column='ADJDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_EQUIPMENTSUB'


class ZmigTjsItem(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20)  # Field name made lowercase.
    item_nm = models.CharField(db_column='ITEM_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    item_unit = models.CharField(db_column='ITEM_UNIT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_std = models.CharField(db_column='ITEM_STD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_prc = models.DecimalField(db_column='ITEM_PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    item_grp_cd = models.CharField(db_column='ITEM_GRP_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_div_cd = models.CharField(db_column='ITEM_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    item_brcd = models.CharField(db_column='ITEM_BRCD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    prnt_item_cd = models.CharField(db_column='PRNT_ITEM_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prnt_cd = models.CharField(db_column='PRNT_CD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vat_cd = models.CharField(db_column='VAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    srvc_chrg = models.DecimalField(db_column='SRVC_CHRG', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    item_tp = models.CharField(db_column='ITEM_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    item_cnt = models.DecimalField(db_column='ITEM_CNT', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    font_color = models.CharField(db_column='FONT_COLOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    discnt_yn = models.CharField(db_column='DISCNT_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prpd_yn = models.CharField(db_column='PRPD_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    point_save_yn = models.CharField(db_column='POINT_SAVE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    point_save_rt = models.DecimalField(db_column='POINT_SAVE_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    point_use_yn = models.CharField(db_column='POINT_USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    disp_yn = models.CharField(db_column='DISP_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    exp_yn = models.CharField(db_column='EXP_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    exp_dy = models.DecimalField(db_column='EXP_DY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_ITEM'


class ZmigTjsItemShopPrice(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20)  # Field name made lowercase.
    item_prc = models.DecimalField(db_column='ITEM_PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_ITEM_SHOP_PRICE'


class ZmigTjsItemSub(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=20)  # Field name made lowercase.
    item_sub_no = models.DecimalField(db_column='ITEM_SUB_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    sub_nm = models.CharField(db_column='SUB_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    item_prc = models.DecimalField(db_column='ITEM_PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    show_yn = models.CharField(db_column='SHOW_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    discnt_yn = models.CharField(db_column='DISCNT_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prpd_yn = models.CharField(db_column='PRPD_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_ITEM_SUB'


class ZmigTjsOrderH(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=40)  # Field name made lowercase.
    ord_dt = models.CharField(db_column='ORD_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ord_tp = models.CharField(db_column='ORD_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ord_stat_cd = models.CharField(db_column='ORD_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tp = models.CharField(db_column='CUST_TP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_qty = models.DecimalField(db_column='CUST_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wait_tm = models.CharField(db_column='WAIT_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trt_tm = models.CharField(db_column='TRT_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trt_mm = models.DecimalField(db_column='TRT_MM', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tot_cost = models.DecimalField(db_column='TOT_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fin_cost = models.DecimalField(db_column='FIN_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_cost = models.DecimalField(db_column='VAT_COST', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ord_info = models.CharField(db_column='ORD_INFO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_no = models.CharField(db_column='RSRV_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mgmt_no = models.CharField(db_column='MGMT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    upsale_yn = models.CharField(db_column='UPSALE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_ORDER_H'


class ZmigTjsOrderL(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    ord_no = models.CharField(db_column='ORD_NO', max_length=20)  # Field name made lowercase.
    ord_line_no = models.DecimalField(db_column='ORD_LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ord_div_cd = models.CharField(db_column='ORD_DIV_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_cd = models.CharField(db_column='ITEM_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_sub_no = models.DecimalField(db_column='ITEM_SUB_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    qt = models.DecimalField(db_column='QT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    prc = models.DecimalField(db_column='PRC', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amt = models.DecimalField(db_column='AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_amt = models.DecimalField(db_column='DISCNT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_tp = models.CharField(db_column='DISCNT_TP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cou_amt = models.DecimalField(db_column='COU_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fin_amt = models.DecimalField(db_column='FIN_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_rt = models.DecimalField(db_column='VAT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_amt = models.DecimalField(db_column='VAT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_cnt = models.DecimalField(db_column='BASE_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bonus_cnt = models.DecimalField(db_column='BONUS_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tot_cnt = models.DecimalField(db_column='TOT_CNT', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_ORDER_L'


class ZmigTjsPayH(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40)  # Field name made lowercase.
    pay_dt = models.CharField(db_column='PAY_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pay_stat_cd = models.CharField(db_column='PAY_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_type_cd = models.CharField(db_column='PAY_TYPE_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_amt = models.DecimalField(db_column='PAY_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_rt = models.DecimalField(db_column='DISCNT_RT', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discnt_amt = models.DecimalField(db_column='DISCNT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tot_amt = models.DecimalField(db_column='TOT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vat_amt = models.DecimalField(db_column='VAT_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rfnd_yn = models.CharField(db_column='RFND_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    apvl_no = models.CharField(db_column='APVL_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_PAY_H'


class ZmigTjsPayMthd(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    pay_no = models.CharField(db_column='PAY_NO', max_length=40)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=3, decimal_places=0)  # Field name made lowercase.
    pay_stat_cd = models.CharField(db_column='PAY_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_type_cd = models.CharField(db_column='PAY_TYPE_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pay_amt = models.DecimalField(db_column='PAY_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='REF_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_line_no = models.DecimalField(db_column='REF_LINE_NO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    apvl_no = models.CharField(db_column='APVL_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_PAY_MTHD'


class ZmigTjsReservationset(models.Model):
    regno = models.IntegerField(db_column='REGNO')  # Field name made lowercase.
    setdiv = models.CharField(db_column='SETDIV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cpcode = models.SmallIntegerField(db_column='CPCODE', blank=True, null=True)  # Field name made lowercase.
    dno = models.CharField(db_column='DNO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rdate = models.CharField(db_column='RDATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rtime = models.CharField(db_column='RTIME', max_length=6, blank=True, null=True)  # Field name made lowercase.
    wset = models.CharField(db_column='WSET', max_length=100, blank=True, null=True)  # Field name made lowercase.
    yset = models.CharField(db_column='YSET', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tset = models.CharField(db_column='TSET', max_length=200, blank=True, null=True)  # Field name made lowercase.
    set1 = models.CharField(db_column='SET1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    set2 = models.CharField(db_column='SET2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    set3 = models.CharField(db_column='SET3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set4 = models.CharField(db_column='SET4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set5 = models.CharField(db_column='SET5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    appyn = models.CharField(db_column='APPYN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reqname = models.CharField(db_column='REQNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regid = models.CharField(db_column='REGID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    aeqname = models.CharField(db_column='AEQNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adjid = models.CharField(db_column='ADJID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adjdate = models.CharField(db_column='ADJDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_RESERVATIONSET'


class ZmigTjsRsrv(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    rsrv_no = models.CharField(db_column='RSRV_NO', max_length=40)  # Field name made lowercase.
    rsrv_div_cd = models.CharField(db_column='RSRV_DIV_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=8)  # Field name made lowercase.
    rsrv_tm = models.CharField(db_column='RSRV_TM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rsrv_drt_mm = models.DecimalField(db_column='RSRV_DRT_MM', max_digits=5, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_cd = models.CharField(db_column='CUST_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_nm = models.CharField(db_column='CUST_NM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cust_tel = models.CharField(db_column='CUST_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cust_qty = models.DecimalField(db_column='CUST_QTY', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_cd = models.CharField(db_column='RSRV_MENU_CD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_menu_nm = models.CharField(db_column='RSRV_MENU_NM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rsrv_memo = models.CharField(db_column='RSRV_MEMO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    rsrv_stat_cd = models.CharField(db_column='RSRV_STAT_CD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rsrv_amt = models.DecimalField(db_column='RSRV_AMT', max_digits=17, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='REF_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ref_id = models.CharField(db_column='REF_ID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_RSRV'


class ZmigTjsRsrvTimeSet(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    line_no = models.DecimalField(db_column='LINE_NO', max_digits=11, decimal_places=0)  # Field name made lowercase.
    dsgn_cd = models.CharField(db_column='DSGN_CD', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rsrv_dt = models.CharField(db_column='RSRV_DT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tset = models.CharField(db_column='TSET', max_length=200, blank=True, null=True)  # Field name made lowercase.
    hbit = models.CharField(db_column='HBIT', max_length=48, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_RSRV_TIME_SET'


class ZmigTjsSaleBox(models.Model):
    shop_cd = models.CharField(db_column='SHOP_CD', max_length=20)  # Field name made lowercase.
    salebox_cd = models.CharField(db_column='SALEBOX_CD', max_length=20)  # Field name made lowercase.
    salebox_nm = models.CharField(db_column='SALEBOX_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sort_seq = models.DecimalField(db_column='SORT_SEQ', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rmk = models.CharField(db_column='RMK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reg_id = models.CharField(db_column='REG_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dtm = models.DateTimeField(db_column='REG_DTM', blank=True, null=True)  # Field name made lowercase.
    upd_id = models.CharField(db_column='UPD_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upd_dtm = models.DateTimeField(db_column='UPD_DTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_SALE_BOX'


class ZmigTjsSetequipment(models.Model):
    div = models.CharField(db_column='DIV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='CLASS', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    info = models.CharField(db_column='INFO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    eqcode = models.CharField(db_column='EQCODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    set1 = models.CharField(db_column='SET1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set2 = models.CharField(db_column='SET2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set3 = models.CharField(db_column='SET3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set4 = models.CharField(db_column='SET4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set5 = models.CharField(db_column='SET5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set6 = models.CharField(db_column='SET6', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set7 = models.CharField(db_column='SET7', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set8 = models.CharField(db_column='SET8', max_length=30, blank=True, null=True)  # Field name made lowercase.
    set9 = models.CharField(db_column='SET9', max_length=700, blank=True, null=True)  # Field name made lowercase.
    set10 = models.CharField(db_column='SET10', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regid = models.CharField(db_column='REGID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='REGDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    adjid = models.CharField(db_column='ADJID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adjdate = models.CharField(db_column='ADJDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZMIG_TJS_SETEQUIPMENT'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Shedlock(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    lock_until = models.DateTimeField(blank=True, null=True)
    locked_at = models.DateTimeField(blank=True, null=True)
    locked_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shedlock'


class SptValues(models.Model):
    name = models.CharField(max_length=35, blank=True, null=True)
    number = models.IntegerField()
    type = models.CharField(max_length=3)
    low = models.IntegerField(blank=True, null=True)
    high = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spt_values'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Test(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'