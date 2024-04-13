from flask import Flask, redirect, url_for, request, render_template
 
app = Flask(__name__)

@app.route('/grantize')
def grantize():
    return render_template('grantize/grantize.html')

@app.route('/logingrantizeoptions')
def logingrantizeoptions():
    return render_template('grantize/login/logingrantizeoptions.html')

@app.route('/logingrantizeres')
def logingrantizeres():
    return render_template('grantize/login/logingrantizeres.html')

@app.route('/logingrantizespo')
def logingrantizespo():
    return render_template('grantize/login/logingrantizespo.html')

@app.route('/createusergrantize')
def createusergrantize():
    return render_template('grantize/login/createusergrantize.html')

@app.route('/grantizewhyus')
def grantizewhyus():
    return render_template('grantize/navbar/whyus.html')

@app.route('/grantizeplans')
def grantizeplans():
    return render_template('grantize/navbar/plans.html')

@app.route('/grantizesponsors')
def grantizesponsors():
    return render_template('grantize/navbar/sponsors.html')

@app.route('/grantizeblogs')
def grantizeblogs():
    return render_template('grantize/navbar/blog.html')

@app.route('/grantizehelp')
def grantizehelp():
    return render_template('grantize/navbar/help.html')

@app.route('/termsnconditions')
def termsnconditions():
    return render_template('grantize/footer/termsnconditions.html')

@app.route('/grantizegrants')
def grantizegrants():
    return render_template('grantize/grants/grants.html')

@app.route('/logingrantizeresdash', methods =["GET", "POST"])
def logingrantizeresdash():
    return render_template('grantize/dashboard/dashboard.html')

@app.route('/grantizeprofile')
def grantizeprofile():
    return render_template('grantize/dashboard/profile.html')

@app.route('/grantizerefreq')
def grantizerefreq():
    return render_template('grantize/dashboard/refrequest.html')

@app.route('/grantizebrowsegrants')
def grantizebrowsegrants():
    return render_template('grantize/dashboard/browsegrants.html')

@app.route('/grantizesearchquery')
def grantizesearchquery():
    return render_template('grantize/dashboard/searchquery.html')

@app.route('/grantizefavquery')
def grantizefavquery():
    return render_template('grantize/dashboard/favquery.html')

@app.route('/grantizesavedquery')
def grantizesavedquery():
    return render_template('grantize/dashboard/savedquery.html')

@app.route('/grantizesharedbyme')
def grantizesharedbyme():
    return render_template('grantize/dashboard/sharedbyme.html')

@app.route('/grantizesharedwithme')
def grantizesharedwithme():
    return render_template('grantize/dashboard/sharedwithme.html')



































@app.route('/recruitphd')
def recruitphd():
    return render_template('recruitphd/recruitphd.html')

@app.route('/recphdwhyus')
def recphdwhyus():
    return render_template('recruitphd/navbar/whyus.html')

@app.route('/recphdplans')
def recphdplans():
    return render_template('recruitphd/navbar/plans.html')

@app.route('/recphdblogs')
def recphdblogs():
    return render_template('recruitphd/navbar/blogs.html')

@app.route('/recphdhelp')
def recphdhelp():
    return render_template('recruitphd/navbar/help.html')

@app.route('/loginrecphdoptions')
def loginrecphdoptions():
    return render_template('recruitphd/login/loginoptions.html')

@app.route('/loginrecphdseeker')
def loginrecphdseeker():
    return render_template('recruitphd/login/loginresearcher.html')

@app.route('/loginrecphdrecruiter')
def loginrecphdrecruiter():
    return render_template('recruitphd/login/loginsponsors.html')

@app.route('/createuserrecphd')
def createuserrecphd():
    return render_template('recruitphd/login/createrecruiter.html')

@app.route('/recphdjobs')
def recphdjobs():
    return render_template('recruitphd/jobs/jobs.html')






























@app.route('/sisterlab')
def sisterlab():
    return render_template('sisterlab/sisterlab.html')

@app.route('/loginsislab')
def loginsislab():
    return render_template('sisterlab/login/loginsislabs.html')

@app.route('/authloginsislab', methods =["GET", "POST"])
def authloginsislab():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email == "admin@gmail.com" and password == "User@123":
            return render_template('sisterlab/dashboard/dashboard.html')
    return render_template('sisterlab/sisterlab.html')

@app.route('/sislabstaff')
def sislabstaff():
    return render_template('sisterlab/dashboard/staff.html')

@app.route('/sislabstaffpermission')
def sislabstaffpermission():
    return render_template('sisterlab/dashboard/staffpermission.html')

@app.route('/sislabactivity')
def sislabactivity():
    return render_template('sisterlab/dashboard/activity.html')

@app.route('/sislabactivitycode')
def sislabactivitycode():
    return render_template('sisterlab/dashboard/activitycode.html')

@app.route('/sislabapplicanttype')
def sislabapplicanttype():
    return render_template('sisterlab/dashboard/applicanttype.html')

@app.route('/sislabawards')
def sislabawards():
    return render_template('sisterlab/dashboard/awards.html')

@app.route('/sislabcfda')
def sislabcfda():
    return render_template('sisterlab/dashboard/cfda.html')

@app.route('/sislabcommittee')
def sislabcommittee():
    return render_template('sisterlab/dashboard/committee.html')

@app.route('/sislabconferences')
def sislabconferences():
    return render_template('sisterlab/dashboard/conferences.html')

@app.route('/sislabdegree')
def sislabdegree():
    return render_template('sisterlab/dashboard/degree.html')

@app.route('/sislabdepartments')
def sislabdepartments():
    return render_template('sisterlab/dashboard/departments.html')

@app.route('/sislabgranttypes')
def sislabgranttypes():
    return render_template('sisterlab/dashboard/granttype.html')

@app.route('/sislabhobbies')
def sislabhobbies():
    return render_template('sisterlab/dashboard/hobbies.html')

@app.route('/sislabjobbenefit')
def sislabjobbenefit():
    return render_template('sisterlab/dashboard/jobbenefits.html')

@app.route('/sislabjournals')
def sislabjournals():
    return render_template('sisterlab/dashboard/journals.html')

@app.route('/sislabkeywords')
def sislabkeywords():
    return render_template('sisterlab/dashboard/keywords.html')

@app.route('/sislablanguages')
def sislablanguages():
    return render_template('sisterlab/dashboard/languages.html')

@app.route('/sislabskillsgained')
def sislabskillsgained():
    return render_template('sisterlab/dashboard/skillsgained.html')

@app.route('/sislabsubjects')
def sislabsubjects():
    return render_template('sisterlab/dashboard/subjects.html')

@app.route('/sislabwtformula')
def sislabwtformula():
    return render_template('sisterlab/dashboard/wtformula.html')

@app.route('/sislabwtforjobs')
def sislabwtforjobs():
    return render_template('sisterlab/dashboard/wtforjobs.html')

@app.route('/sislabskillsets')
def sislabskillsets():
    return render_template('sisterlab/dashboard/skillsets.html')

@app.route('/sislablocations')
def sislablocations():
    return render_template('sisterlab/dashboard/skillsets.html')

@app.route('/sislabgrants')
def sislabgrants():
    return render_template('sisterlab/grantize/grants.html')

@app.route('/sislabsponsors')
def sislabsponsors():
    return render_template('sisterlab/grantize/sponsors.html')

@app.route('/sislabresearchers')
def sislabresearchers():
    return render_template('sisterlab/grantize/researchers.html')

@app.route('/sislabsponsorplan')
def sislabsponsorplan():
    return render_template('sisterlab/grantize/sponsorplan.html')

@app.route('/sislabresearcherplan')
def sislabresearcherplan():
    return render_template('sisterlab/grantize/researcherplan.html')

@app.route('/sislabnotifications')
def sislabnotifications():
    return render_template('sisterlab/grantize/notifications.html')

@app.route('/sislabbanners')
def sislabbanners():
    return render_template('sisterlab/grantize/banners.html')

@app.route('/sislabtestimonials')
def sislabtestimonials():
    return render_template('sisterlab/grantize/testimonials.html')

@app.route('/sislabvidtestimonials')
def sislabvidtestimonials():
    return render_template('sisterlab/grantize/vidtestimonials.html')

@app.route('/sislabwhygrant')
def sislabwhygrant():
    return render_template('sisterlab/grantize/whyus.html')

@app.route('/sislabgrantblogs')
def sislabgrantblogs():
    return render_template('sisterlab/grantize/blogs.html')

@app.route('/sislabgrantfaqs')
def sislabgrantfaqs():
    return render_template('sisterlab/grantize/faq.html')

@app.route('/sislabgrantpages')
def sislabgrantpages():
    return render_template('sisterlab/grantize/pages.html')

@app.route('/sislabrecjobs')
def sislabrecjobs():
    return render_template('sisterlab/recruitphd/jobs.html')

@app.route('/sislabrecjobapplications')
def sislabrecjobapplications():
    return render_template('sisterlab/recruitphd/jobapplications.html')

@app.route('/sislabrecrecruiters')
def sislabrecrecruiters():
    return render_template('sisterlab/recruitphd/recruiters.html')

@app.route('/sislabrecseekers')
def sislabrecseekers():
    return render_template('sisterlab/recruitphd/jobseekers.html')

@app.route('/sislabrecplans')
def sislabrecplans():
    return render_template('sisterlab/recruitphd/plans.html')

@app.route('/sislabrecplanseeker')
def sislabrecplanseeker():
    return render_template('sisterlab/recruitphd/jobseekers.html')

@app.route('/sislabrecnotifications')
def sislabrecnotifications():
    return render_template('sisterlab/recruitphd/notifications.html')

@app.route('/sislabrecbanners')
def sislabrecbanners():
    return render_template('sisterlab/recruitphd/banners.html')

@app.route('/sislabrectestimonials')
def sislabrectestimonials():
    return render_template('sisterlab/recruitphd/testimonials.html')

@app.route('/sislabrectestimonialsvideo')
def sislabrectestimonialsvideo():
    return render_template('sisterlab/recruitphd/videotestimonials.html')

@app.route('/sislabrecwhyus')
def sislabrecwhyus():
    return render_template('sisterlab/recruitphd/whyus.html')

@app.route('/sislabrecblogs')
def sislabrecblogs():
    return render_template('sisterlab/recruitphd/blogs.html')

@app.route('/sislabrecfaqs')
def sislabrecfaqs():
    return render_template('sisterlab/recruitphd/faq.html')

@app.route('/sislabrecpages')
def sislabrecpages():
    return render_template('sisterlab/recruitphd/pages.html')






 
# main driver function
if __name__ == '__main__':
    app.run(port = 6991, debug = True)