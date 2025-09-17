from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Project(models.Model):
    FINANCING_TYPES = [
        ('internal_financing', 'تمويل داخلي'),
        ('major_subscribers', 'كبار المشتركين'),
    ]
    PROJECT_CATEGORY_EN_CHOICES = [
        ('high_voltage', 'High Voltage'),
        ('extra_high_voltage', 'Extra High Voltage'),
    ]
    SIGNING_AUTHORITIES = [
        ('sec', 'SEC'),
        ('customer', 'Customer'),
    ]
    PROJECT_PHASES = [
        ('under_implementation', 'قيد التنفيذ'),
        ('implemented', 'تم التنفيذ'),
    ]
    contract_number = models.CharField(
        'رقم العقد',
        max_length=20
    )
    project_name = models.CharField(
        'إسم المشروع',
        max_length=100
    )
    original_contract_value = models.FloatField(
        'قيمة العقد الأصلية',
        validators=[MinValueValidator(0.0)]
    )
    contract_signing_date = models.DateField(
        'تاريخ توقيع العقد'
    )
    project_account_no_1 = models.CharField(
        'رقم حساب المشروع ١',
        max_length=20,
        null=True,
        blank=True
    )
    contractor_name = models.CharField(
        'إسم المقاول',
        max_length=100
    )
    financing_type = models.CharField(
        'نوع التمويل',
        max_length=20,
        choices=FINANCING_TYPES,
        default='internal_financing'
    )
    funding_source = models.CharField(
        'مصدر التمويل',
        max_length=100,
        null=True,
        blank=True
    )
    project_type = models.CharField(
        'نوع المشروع',
        max_length=50
    )
    project_category_en = models.CharField(
        'Project_Category_En',
        max_length=20,
        choices=PROJECT_CATEGORY_EN_CHOICES,
        default='high_voltage'
    )
    project_engineer = models.CharField(
        'مهندس المشروع',
        max_length=100,
    )
    department = models.CharField(
        'الدائرة',
        max_length=100,
    )
    emirate = models.CharField(
        'الإمارة',
        max_length=50,
    )
    city = models.CharField(
        'المدينة',
        max_length=50
    )
    signing_authority = models.CharField(
        'جهة التوقيع',
        max_length=20,
        choices=SIGNING_AUTHORITIES,
        default='sec'
    )
    site_handover_date = models.DateField(
        'تاريخ تسليم الموقع',
        null=True,
        blank=True,
    )
    project_phase = models.CharField(
        'مرحلة المشروع',
        max_length=50,
        choices=PROJECT_PHASES,
        default='under_implementation'
    )
    expected_operation_date = models.DateField(
        'تاريخ التشغيل (متوقع)'
    )
    contractual_technical_completion_date = models.DateField(
        'تاريخ الإنجاز الفني (تعاقدي)',
        null=True,
        blank=True
    )
    contractual_provisional_acceptance_date = models.DateField(
        'تاريخ الإستلام الإبتدائي (تعاقدي)',
        null=True,
        blank=True
    )
    contractual_final_acceptance_date = models.DateField(
        'تاريخ الإستلام النهائي (تعاقدي)',
        null=True,
        blank=True
    )
    expected_provisional_acceptance_date = models.DateField(
        'تاريخ الإستلام الإبتدائي (متوقع)',
        null=True,
        blank=True
    )
    expected_final_acceptance_date = models.DateField(
        'تاريخ الإستلام النهائي (متوقع)',
        null=True,
        blank=True
    )
    actual_technical_completion_date = models.DateField(
        'تاريخ الإنجاز الفني (فعلي)',
        null=True,
        blank=True
    )
    actual_provisional_acceptance_date = models.DateField(
        'تاريخ الإستلام الإبتدائي (فعلي)',
        null=True,
        blank=True
    )
    actual_final_acceptance_date = models.DateField(
        'تاريخ الإستلام النهائي (فعلي)',
        null=True,
        blank=True
    )
    actual_progress_percentage = models.FloatField(
        'نسبة الإنجاز (فعلي)',
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    planned_progress_percentage = models.FloatField(
        'نسبة الإنجاز (مخطط)',
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.contract_number

    class Meta:
        verbose_name = 'المشروع'
        verbose_name_plural = 'المشاريع'
