"""
Pathways for the Odonto RMS
"""
import datetime

from opal.core.pathways import PagePathway, Step
from rms import models
from opal import models as omodels


class ReferralPathway(PagePathway):
    display_name = "Referral"
    slug = "referral_form"
    step_wrapper_template_url = "/templates/pathways/step_wrappers/odonto_page_wrapper.html"
    template_url = "/templates/pathways/odonto_pathway_base.html"

    steps = (
        Step(
            display_name='Patient Details',
            template_url="/templates/pathways/steps/patient_detail.html"
        ),
        models.CarerDetails,
        models.GPDetails,
        models.ReferralReason,
        models.Xray,
        models.Disability,
        models.MedicalIssues,
        models.MentalHealthIssues,
    )

    def save(self, data, user):
        data[models.Demographics.get_api_name()][0]["hospital_number"] = omodels.Patient.objects.count()
        patient = super(ReferralPathway, self).save(data, user)
        episode = patient.episode_set.last()
        episode.active = True
        episode.save()
        referral = episode.referraldetails_set.first()
        referral.when = datetime.date.today()
        referral.who = user
        referral.save()
        return patient

    def redirect_url(self, patient):
        episode = patient.episode_set.last()
        return '/#/patient/{0}/{1}'.format(patient.id, episode.id)


class CheckAndFind(PagePathway):
    display_name = "Check and find"
    slug = "check_and_find"
    steps = (models.AllocatedClinic,)


class ApproveDecision(PagePathway):
    _is_singleton = True
    display_name = "Approve"
    slug = "approve"
    steps = (models.AllocatedClinic,)
