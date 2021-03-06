# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-15 18:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0025_auto_20180112_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allergies',
            options={'verbose_name_plural': 'Allergies'},
        ),
        migrations.AlterModelOptions(
            name='demographics',
            options={'verbose_name_plural': 'Demographics'},
        ),
        migrations.AlterModelOptions(
            name='diagnosis',
            options={'verbose_name_plural': 'Diagnoses'},
        ),
        migrations.AlterModelOptions(
            name='pastmedicalhistory',
            options={'verbose_name_plural': 'Past medical histories'},
        ),
        migrations.AlterField(
            model_name='allergies',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_allergies_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='allergies',
            name='drug_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Drug'),
        ),
        migrations.AlterField(
            model_name='allergies',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_allergies_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='allocatedclinic',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_allocatedclinic_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='allocatedclinic',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_allocatedclinic_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carerdetails',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_carerdetails_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='carerdetails',
            name='relationship_to_patient_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rms.RelationshipToPatient'),
        ),
        migrations.AlterField(
            model_name='carerdetails',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_carerdetails_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contactdetails',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_contactdetails_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contactdetails',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_contactdetails_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='birth_place_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Destination'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_demographics_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='ethnicity_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Ethnicity'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='marital_status_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.MaritalStatus'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='sex_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Gender'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='title_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Title'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_demographics_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='condition_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Condition'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_diagnosis_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_diagnosis_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='disability',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_disability_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='disability',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_disability_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gpdetails',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_gpdetails_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gpdetails',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_gpdetails_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='investigation',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_investigation_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='investigation',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_investigation_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='location',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_location_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='location',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_location_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='medicalissues',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_medicalissues_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='medicalissues',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_medicalissues_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='medication',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_medication_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='medication',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_medication_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mentalhealthissues',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_mentalhealthissues_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mentalhealthissues',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_mentalhealthissues_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pastmedicalhistory',
            name='condition_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Condition'),
        ),
        migrations.AlterField(
            model_name='pastmedicalhistory',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_pastmedicalhistory_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pastmedicalhistory',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_pastmedicalhistory_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patientconsultation',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_patientconsultation_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patientconsultation',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_patientconsultation_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='referraldetails',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_referraldetails_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='referraldetails',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_referraldetails_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='referralreason',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_referralreason_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='referralreason',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_referralreason_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='requestfurtherinformation',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_requestfurtherinformation_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='requestfurtherinformation',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_requestfurtherinformation_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='symptomcomplex',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_symptomcomplex_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='symptomcomplex',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_symptomcomplex_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_treatment_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='drug_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Drug'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='frequency_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Drugfreq'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='route_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Drugroute'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_treatment_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='xray',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rms_xray_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='xray',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_rms_xray_subrecords', to=settings.AUTH_USER_MODEL),
        ),
    ]
