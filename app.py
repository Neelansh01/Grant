from flask import Flask, session, redirect, url_for, request, render_template, jsonify, send_file, flash
from datetime import timedelta
import mysql.connector
import base64
from io import BytesIO
from datetime import datetime
import mimetypes
from werkzeug.utils import secure_filename


 
app = Flask(__name__)
app.secret_key = 'Grant####secret***my_hard_to_crack_secret_key'
app.permanent_session_lifetime = timedelta(hours=3)
sqlconnection = ""







@app.route('/grantize')
def grantize():
    session.clear()
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

@app.route('/registerresgrantize', methods =["GET", "POST"])
def registerresgrantize():
    global sqlconnection
    print("ENTER REGISTER FUNCTION")
    if "_tokenpersonal" in request.form:
        try:
            name_prefix = request.form['name_prefix']
            fname = request.form['fname']
            lname = request.form['lname']
            qualification = request.form['qualification']
            email = request.form['email_personal']
            mobile = request.form['mobile']
            username = request.form['uname']
            password = request.form['password']
            addl1 = request.form['address_line_one']
            addl2 = request.form['address_line_two']
            postcode = request.form['post_code']
            country = request.form['country']
            state = request.form['state']
            city = request.form['city']
        except:
            print("REGISTER USER VARIABLES COULD NOT BE READ!!")
            return render_template('grantize/grantize.html')
        mycursor = sqlconnection.cursor()
        sql = "INSERT INTO gresearcherslist (prefix, firstname, lastname, qualification, email, mobile, username, password, addressline1, addressline2, postcode, country, state, city) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (name_prefix, fname, lname, qualification, email, mobile, username, password, addl1, addl2, postcode, country, state, city)
        try:
            mycursor.execute(sql, val)
            sqlconnection.commit()
            mycursor.close()
            print("Database Insertion Successful....")
        except:
            print("Database Insertion Failed!!")
        return render_template('grantize/dashboard/dashboard.html')
    elif "_tokenmanager" in request.form:
        try:
            organization = request.form['organization']
            email_prefix = request.form['email_prefix']
            email_domain = request.form['email_domain']
            email_institutional = request.form['email_institutional']
            fname = request.form['fname']
            lname = request.form['lname']
            email_personal = request.form['email_personal']
            mobile = request.form['mobile']
            uname = request.form['uname']
            password = request.form['password']
            address_line_one = request.form['address_line_one']
            address_line_two = request.form['address_line_two']
            post_code = request.form['post_code']
            country = request.form['country']
            state = request.form['state']
            city = request.form['city']
        except:
            print("REGISTER USER VARIABLES COULD NOT BE READ!!")
            return render_template('grantize/grantize.html')
        mycursor = sqlconnection.cursor()
        sql = "INSERT INTO gmanagerslist (organization, email_prefix, email_domain, email_institutional, fname, lname, email_personal, mobile, uname, password, address_line_one, address_line_two, postcode, country, state, city) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (organization, email_prefix, email_domain, email_institutional, fname, lname, email_personal, mobile, uname, password, address_line_one, address_line_two, post_code, country, state, city)
        try:
            mycursor.execute(sql, val)
            sqlconnection.commit()
            mycursor.close()
            print("Database Insertion Successful....")
        except:
            print("Database Insertion Failed!!")
        return render_template('grantize/dashboard/dashboard.html')
    else:
        return render_template('grantize/dashboard/dashboard.html')


@app.route('/logingrantizeresdash', methods =["GET", "POST"])
def logingrantizeresdash():
    global sqlconnection
    print("ENTER DASHBOARD FUNCTION")
    if not session.get("loginnname"):
        if "_tokenresearcher" in request.form:
            try:
                username = request.form['user_name']
                password = request.form['pass_word']
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/grantize.html')
            mycursor = sqlconnection.cursor()
            sql = "SELECT * FROM gmanagerslist WHERE uname = %s AND password = %s"
            values = (username, password)
            mycursor.execute(sql, values)
            result = mycursor.fetchall()
            if result:
                print("Match Found..")
                session["loginnname"] = username
                session["loginid"] = result[0][0]
                print(session.get('loginid'))
                return render_template('grantize/dashboard/dashboard.html')
            else:
                print("Match Not Found..")
                return render_template('grantize/grantize.html')
        elif "_tokensponsor" in request.form:
            try:
                username = request.form['user_name']
                password = request.form['pass_word']
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/grantize.html')
            mycursor = sqlconnection.cursor()
            sql = "SELECT id FROM gsponsorslist WHERE username = %s AND password = %s"
            values = (username, password)
            mycursor.execute(sql, values)
            result = mycursor.fetchall()
            if result:
                print("Match Found..")
                session["loginnname"] = username
                session["loginid"] = result[0][0]
                print(session.get('loginid'))
                return render_template('grantize/dashboard/dashboard.html')
            else:
                print("Match Not Found..")
                return render_template('grantize/grantize.html')
        else:
            return render_template('grantize/grantize.html')
    else:
        return render_template('grantize/dashboard/dashboard.html')
    
@app.route('/grantizelogout')
def grantizelogout():
    if session.get("loginnname"):
        session.pop("loginnname")
        session.pop("loginid")
        session.clear()
        return render_template('grantize/grantize.html')
    else:
        return render_template('grantize/grantize.html')

@app.route('/grantizeprofile')
def grantizeprofile():
    if session.get("loginnname"):
        return render_template('grantize/dashboard/profile.html')
    else:
        return render_template('grantize/grantize.html')

@app.route('/grantizeprofilesummary')
def grantizeprofilesummary():
    if session.get("loginnname"):
        return render_template('grantize/profile/summary.html')
    else:
        return render_template('grantize/grantize.html')

@app.route('/grantizeprofileobjective')
def grantizeprofileobjective():
    if session.get("loginnname"):
        return render_template('grantize/profile/objective.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofileresstatement')
def grantizeprofileresstatement():
    if session.get("loginnname"):
        return render_template('grantize/profile/resstatement.html')
    else:
        return render_template('grantize/grantize.html')
    

@app.route('/grantizeprofileteachphil')
def grantizeprofileteachphil():
    if session.get("loginnname"):
        return render_template('grantize/profile/teachphilosophy.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofileeducation')
def grantizeprofileeducation():
    if session.get("loginnname"):
        return render_template('grantize/profile/education.html')
    else:
        return render_template('grantize/grantize.html')

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'pdf', 'docx'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def cred_read_table(user):
    global sqlconnection
    # SQL query to get all files and other data with condition "WHERE 1=1"
    mycursor = sqlconnection.cursor()
    query = "SELECT description, organization, filename, id FROM gcredentials WHERE userid = "+str(user)
    mycursor.execute(query)
    rows = mycursor.fetchall()
    documents = []
    # Prepare each row with base64 encoding for the file
    for row in rows:
        documents.append({
            'description': row[0],
            'organization': row[1],
            'filename' : row[2],
            'id' : row[3]
        })
    mycursor.close()
    return documents

@app.route('/download/<filename>')
def download_file(filename):
    global sqlconnection
    cursor = sqlconnection.cursor()
    try:
        # Prepare a query to fetch the file data by name
        query = "SELECT filename, filecontent FROM gcredentials WHERE filename = %s"
        cursor.execute(query, (filename,))
        file_data = cursor.fetchone()
        if file_data is None:
            return jsonify({'error': 'File not found'}), 404

        # Secure the filename to prevent path traversal attacks
        filename = secure_filename(file_data[0])

        # Guess the MIME type of the file based on its extension
        mime_type, _ = mimetypes.guess_type(filename)
        if mime_type is None:
            mime_type = 'application/octet-stream'  # Fallback to binary type if MIME type is undetectable

        # Send the file data as an attachment
        file_stream = BytesIO(file_data[1])
        return send_file(
            file_stream,
            mimetype=mime_type,
            as_attachment=True,
            download_name=filename
        )
    except mysql.connector.Error as err:
        print("Error: ", err)
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()

def prmission_show_me(main_table, except_persons, user):
    global sqlconnection
    try:
        mycursor = sqlconnection.cursor()
        sql = "UPDATE "+main_table+" SET showme = '"+except_persons+"' WHERE userid = "+str(user)
        mycursor.execute(sql)
        sqlconnection.commit()
        mycursor.close()
    except:
        print("Database Operation Failed!!")

def prmission_hide_designation(main_table, multiselect, user):
    global sqlconnection
    try:
        except_persons = ",".join(multiselect)
        mycursor = sqlconnection.cursor()
        sql = "UPDATE "+main_table+" SET hidedesignation = '"+except_persons+"' WHERE userid = "+str(user)
        mycursor.execute(sql)
        sqlconnection.commit()
        mycursor.close()

    except:
        print("Database Operation Failed!!")

def prmission_hide_individuals(main_table, except_persons, user):
    global sqlconnection
    try:
        mycursor = sqlconnection.cursor()
        sql = "UPDATE "+main_table+" SET hideindividuals = '"+except_persons+"' WHERE userid = "+str(user)
        mycursor.execute(sql)
        sqlconnection.commit()
        mycursor.close()
    except:
        print("Database Operation Failed!!")

@app.route('/grantizeprofilerescredentials', methods =["GET", "POST"])
def grantizeprofilerescredentials():
    if session.get("loginnname"):
        user = session.get('loginid')
        if "addcredtrans" in request.form:
            try:
                credname, credorg, credfiles, credfilename = None, None, None, None
                if 'name' in request.form:
                    credname = request.form['name']
                if 'organization' in request.form:
                    credorg = request.form['organization']
                if 'filecred' in request.files and request.files['filecred'].filename != '' and allowed_file(request.files['filecred'].filename):
                    credfiles = request.files['filecred']
                    file_content = credfiles.read()
                    credfilename = secure_filename(credfiles.filename)
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/credentials.html')
            try:
                mycursor = sqlconnection.cursor()
                sql = "INSERT INTO gcredentials (userid, description, organization, filename, filecontent) VALUES (%s, %s, %s, %s, %s)"
                values = (user, credname, credorg, credfilename, file_content)
                mycursor.execute(sql, values)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("DATBASE FAILURE!!")
                return render_template('grantize/profile/credentials.html')
            ## Code to Read
            documents = cred_read_table(user)
            return render_template('grantize/profile/credentials.html', documents=documents)
        if "editform" in request.form:
            try:
                cred_id = request.form['credid']
                updates = []
                values = []

                # Check each field and add to the update statement if present
                if 'name' in request.form and request.form['name']:
                    updates.append("description = %s")
                    values.append(request.form['name'])

                if 'organization' in request.form and request.form['organization']:
                    updates.append("organization = %s")
                    values.append(request.form['organization'])

                # Handle file upload
                if 'changefile' in request.files and request.files['changefile'].filename != '' and allowed_file(request.files['changefile'].filename):
                    credfile = request.files['changefile']
                    file_content = credfile.read()
                    credfilename = secure_filename(credfile.filename)
                    updates.append("filename = %s")
                    values.append(credfilename)
                    updates.append("filecontent = %s")
                    values.append(file_content)
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/credentials.html')
            try:
                if updates:
                    sql = f"UPDATE gcredentials SET {', '.join(updates)} WHERE id = %s"
                    print(sql)
                    print(cred_id)
                    print(updates)
                    values.append(cred_id)
                    mycursor = sqlconnection.cursor()
                    mycursor.execute(sql, tuple(values))
                    sqlconnection.commit()
                    mycursor.close()
            except:
                print("DATBASE FAILURE!!")
                return render_template('grantize/profile/credentials.html')
            ## Code to Read
            documents = cred_read_table(user)
            return render_template('grantize/profile/credentials.html', documents=documents)
        if "permissions" in request.form:
            try:
                if request.form.get("public"):
                    except_persons = request.form['except_persons']
                    prmission_show_me('gcredentials',except_persons, user)
                if request.form.get("designation"):
                    except_persons = request.form.getlist('designations')
                    prmission_hide_designation('gcredentials', except_persons, user)
                if request.form.get("person"):
                    except_persons = request.form['except_invidividuals']
                    prmission_hide_individuals('gcredentials', except_persons, user)
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/credentials.html')
            try:
                mycursor = sqlconnection.cursor()
                sql = "INSERT INTO gcredentials (userid, description, organization, filename, filecontent) VALUES (%s, %s, %s, %s, %s)"
                values = (user, credname, credorg, credfilename, file_content)
                mycursor.execute(sql, values)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("DATBASE FAILURE!!")
                return render_template('grantize/profile/credentials.html')
            ## Code to Read
            documents = cred_read_table(user)
            return render_template('grantize/profile/credentials.html', documents=documents)
        if "delete" in request.form:
            try:
                id_to_delete = request.form['document_id']
                mycursor = sqlconnection.cursor()
                sql = "DELETE FROM gcredentials WHERE id = "+str(id_to_delete)
                mycursor.execute(sql)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/credentials.html')
            ## Code to Read
            documents = cred_read_table(user)
            return render_template('grantize/profile/credentials.html', documents=documents)
        else:
            documents = cred_read_table(user)
            return render_template('grantize/profile/credentials.html', documents=documents)
    else:
        return render_template('grantize/grantize.html')


def work_experience_read_table(user):
    global sqlconnection
    try:
        mycursor = sqlconnection.cursor(dictionary=True)
        # SQL query to get all columns except 'id' and 'userid'
        query = """
        SELECT id, employer, department, type, appoint, title, 
                current, start, end, mentor, responsibilities, rkeywords,
                techniques, skilldesc, skeywords, instruments, softwares, softskills
        FROM gexperience
        WHERE userid = %s
        """
        mycursor.execute(query, (user,))
        rows = mycursor.fetchall()
        
        # Convert rows to a list of dictionaries for easy handling in the template
        experiences = []
        for row in rows: 
            experiences.append(row)
            
        mycursor.close()
        return experiences
    except Exception as e:
        print("Error fetching work experience from database:", str(e))
        return []


@app.route('/grantizeprofileexperience', methods =["GET", "POST"])
def grantizeprofileexperience():
    if session.get("loginnname"):
        user = session.get('loginid')
        if "createexp" in request.form:
            print("_________________STEP 0__________________")
            try:
                # Helper function to get the form data or return None if blank
                def get_form_data_or_none(field_name):
                    return request.form[field_name] if field_name in request.form and request.form[field_name].strip() else None

                # Retrieve form data
                employer_name = get_form_data_or_none('organization')
                department = get_form_data_or_none('department')
                job_type = get_form_data_or_none('type')
                appoint_type = get_form_data_or_none('name')
                job_title = get_form_data_or_none('title')
                current_job = request.form['is_this_current_job'] if 'is_this_current_job' in request.form else None
                start_date = get_form_data_or_none('start_date')
                end_date = get_form_data_or_none('end_date')
                mentor_name = get_form_data_or_none('mentors')
                main_responsibilities = get_form_data_or_none('description2')
                keyword_abstract = get_form_data_or_none('keyword_abstract')
                techniques = get_form_data_or_none('techniques')
                instruments = get_form_data_or_none('instruments')
                softwares = get_form_data_or_none('softwares')
                soft_skills = get_form_data_or_none('soft_skills')
                key_skills_experience = ','.join(filter(None, request.form.getlist('description')))
                keyword_description = get_form_data_or_none('keyword_description')
                start_date = datetime.strptime(start_date, '%m-%d-%Y').date()
                end_date = datetime.strptime(end_date, '%m-%d-%Y').date()
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/experience.html')
            print("_________________STEP 1__________________")
            try:
                mycursor = sqlconnection.cursor()
                sql = """
                INSERT INTO gexperience
                (userid, employer, department, type, appoint, title, 
                current, start, end, mentor, responsibilities, rkeywords,
                techniques, skilldesc, skeywords, instruments, softwares, softskills)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = [user, employer_name, department, job_type, appoint_type, job_title,
                        current_job, start_date, end_date, mentor_name, main_responsibilities, 
                        keyword_abstract, techniques, key_skills_experience, keyword_description,
                        instruments, softwares, soft_skills]
                for i in range(len(values)):
                    if values[i] == None:
                        values[i] = ""
                values = tuple(values)
                print(values)
                mycursor.execute(sql, values)
                sqlconnection.commit()
                mycursor.close()
                print("_________________STEP 3__________________")
                flash('Work experience added successfully!', 'success')
            except:
                print("DATBASE FAILURE!!")
                return render_template('grantize/profile/experience.html')
            ## Code to Read
            documents = work_experience_read_table(user)
            return render_template('grantize/profile/experience.html', documents = documents)
        if "editsection" in request.form:
            try:
                print("_________________EDIT STEP 0__________________")
                experience_id = request.form['document_id']
                updates = []
                values = []

                # Helper function to get form data or None
                def get_form_data_or_none(field):
                    return request.form[field].strip() if field in request.form and request.form[field].strip() else None

                # Define the mapping from form fields to database columns
                form_to_db_map = {
                    'organization': 'employer',
                    'department': 'department',
                    'type': 'type',
                    'name': 'appoint',
                    'title': 'title',
                    'is_this_current_job': 'current',
                    # Assuming dates are in 'MM-DD-YYYY' format, we parse them to 'YYYY-MM-DD' format for SQL
                    'start_date': ('start', lambda x: datetime.strptime(x, '%m-%d-%Y').strftime('%Y-%m-%d') if x else None),
                    'end_date': ('end', lambda x: datetime.strptime(x, '%m-%d-%Y').strftime('%Y-%m-%d') if x else None),
                    'mentors': 'mentor',
                    'description2': 'responsibilities',
                    'keyword_abstract': 'rkeywords',
                    'techniques': 'techniques',
                    'instruments': 'instruments',
                    'softwares': 'softwares',
                    'soft_skills': 'softskills',
                    'description': 'skilldesc',
                    'keyword_description': 'skeywords'
                }

                # Loop over the fields and prepare SQL update statement
                for form_field, db_info in form_to_db_map.items():
                    # db_info can be either a string or a tuple (column_name, transform_function)
                    db_column, transform = db_info if isinstance(db_info, tuple) else (db_info, None)
                    form_data = get_form_data_or_none(form_field)
                    if form_data is not None:
                        updates.append(f"{db_column} = %s")
                        # Apply transformation function if provided
                        values.append(transform(form_data) if transform else form_data)
                print("_________________STEP 1__________________")
                if updates:
                    update_sql = ", ".join(updates)
                    sql = f"UPDATE gexperience SET {update_sql} WHERE id = %s"
                    values.append(experience_id)
                    print(update_sql)
                    print(experience_id)
                    print(sql)
                    mycursor = sqlconnection.cursor()
                    mycursor.execute(sql, tuple(values))
                    sqlconnection.commit()
                    mycursor.close()
                    print("_________________STEP 2 EDIT__________________")
                    flash('Experience updated successfully!', 'success')
                else:
                    flash('No changes to update.', 'info')

            except Exception as e:
                flash('Failed to update experience due to an error.', 'error')
                print(f"Error updating experience: {e}")
                return render_template('error_template.html'), 500
            ## Code to Read
            documents = work_experience_read_table(user)
            return render_template('grantize/profile/experience.html', documents = documents)
        if "permissions" in request.form:
            try:
                if request.form.get("public"):
                    except_persons = request.form['except_persons']
                    prmission_show_me('gcredentials',except_persons, user)
                if request.form.get("designation"):
                    except_persons = request.form.getlist('designations')
                    prmission_hide_designation('gcredentials', except_persons, user)
                if request.form.get("person"):
                    except_persons = request.form['except_invidividuals']
                    prmission_hide_individuals('gcredentials', except_persons, user)
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/credentials.html')
            try:
                mycursor = sqlconnection.cursor()
                sql = "INSERT INTO gcredentials (userid, description, organization, filename, filecontent) VALUES (%s, %s, %s, %s, %s)"
                values = (user, credname, credorg, credfilename, file_content)
                mycursor.execute(sql, values)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("DATBASE FAILURE!!")
                return render_template('grantize/profile/credentials.html')
            ## Code to Read
            documents = cred_read_table(user)
            return render_template('grantize/profile/credentials.html', documents=documents)
        if "delete" in request.form:
            try:
                id_to_delete = request.form['id']
                print("-------------")
                print(id_to_delete)
                print("--------------")
                mycursor = sqlconnection.cursor()
                sql = "DELETE FROM gexperience WHERE id = "+str(id_to_delete)
                mycursor.execute(sql)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/credentials.html')
            ## Code to Read
            documents = work_experience_read_table(user)
            return render_template('grantize/profile/experience.html', documents = documents)
        else:
            documents = work_experience_read_table(user)
            print(documents)
            return render_template('grantize/profile/experience.html', documents = documents)
    else:
        return render_template('grantize/grantize.html')
    
def volunteer_read_table(user):
    global sqlconnection
    try:
        mycursor = sqlconnection.cursor(dictionary=True)
        # SQL query to get all columns except 'id' and 'userid'
        query = """
        SELECT id, employer, department, type, appoint, title, 
                current, start, end, mentor, responsibilities, rkeywords,
                techniques, skilldesc, skeywords, instruments, softwares, softskills
        FROM gvolunteer
        WHERE userid = %s
        """
        mycursor.execute(query, (user,))
        rows = mycursor.fetchall()
        
        # Convert rows to a list of dictionaries for easy handling in the template
        experiences = []
        for row in rows: 
            experiences.append(row)
            
        mycursor.close()
        return experiences
    except Exception as e:
        print("Error fetching work experience from database:", str(e))
        return []

@app.route('/grantizeprofilevolunteer', methods =["GET", "POST"])
def grantizeprofilevolunteer():
    global sqlconnection
    if session.get("loginnname"):
        user = session.get('loginid')
        if "createexp" in request.form:
            print("_________________STEP 0__________________")
            try:
                # Helper function to get the form data or return None if blank
                def get_form_data_or_none(field_name):
                    return request.form[field_name] if field_name in request.form and request.form[field_name].strip() else None

                # Retrieve form data
                employer_name = get_form_data_or_none('organization')
                department = get_form_data_or_none('department')
                job_type = get_form_data_or_none('type')
                appoint_type = get_form_data_or_none('name')
                job_title = get_form_data_or_none('title')
                current_job = request.form['is_this_current_job'] if 'is_this_current_job' in request.form else None
                start_date = get_form_data_or_none('start_date')
                end_date = get_form_data_or_none('end_date')
                mentor_name = get_form_data_or_none('mentors')
                main_responsibilities = get_form_data_or_none('description2')
                keyword_abstract = get_form_data_or_none('keyword_abstract')
                techniques = get_form_data_or_none('techniques')
                instruments = get_form_data_or_none('instruments')
                softwares = get_form_data_or_none('softwares')
                soft_skills = get_form_data_or_none('soft_skills')
                key_skills_experience = ','.join(filter(None, request.form.getlist('description')))
                keyword_description = get_form_data_or_none('keyword_description')
                start_date = datetime.strptime(start_date, '%m-%d-%Y').date()
                end_date = datetime.strptime(end_date, '%m-%d-%Y').date()
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/volunteer.html')
            print("_________________STEP 1__________________")
            try:
                mycursor = sqlconnection.cursor()
                sql = """
                INSERT INTO gvolunteer
                (userid, employer, department, type, appoint, title, 
                current, start, end, mentor, responsibilities, rkeywords,
                techniques, skilldesc, skeywords, instruments, softwares, softskills)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = [user, employer_name, department, job_type, appoint_type, job_title,
                        current_job, start_date, end_date, mentor_name, main_responsibilities, 
                        keyword_abstract, techniques, key_skills_experience, keyword_description,
                        instruments, softwares, soft_skills]
                for i in range(len(values)):
                    if values[i] == None:
                        values[i] = ""
                values = tuple(values)
                print(values)
                mycursor.execute(sql, values)
                sqlconnection.commit()
                mycursor.close()
                print("_________________STEP 3__________________")
                flash('Work experience added successfully!', 'success')
            except:
                print("DATBASE FAILURE!!")
                return render_template('grantize/profile/volunteer.html')
            ## Code to Read
            documents = volunteer_read_table(user)
            return render_template('grantize/profile/volunteer.html', documents = documents)
        if "editsection" in request.form:
            try:
                print("_________________EDIT STEP 0__________________")
                experience_id = request.form['document_id']
                updates = []
                values = []

                # Helper function to get form data or None
                def get_form_data_or_none(field):
                    return request.form[field].strip() if field in request.form and request.form[field].strip() else None

                # Define the mapping from form fields to database columns
                form_to_db_map = {
                    'organization': 'employer',
                    'department': 'department',
                    'type': 'type',
                    'name': 'appoint',
                    'title': 'title',
                    'is_this_current_job': 'current',
                    # Assuming dates are in 'MM-DD-YYYY' format, we parse them to 'YYYY-MM-DD' format for SQL
                    'start_date': ('start', lambda x: datetime.strptime(x, '%m-%d-%Y').strftime('%Y-%m-%d') if x else None),
                    'end_date': ('end', lambda x: datetime.strptime(x, '%m-%d-%Y').strftime('%Y-%m-%d') if x else None),
                    'mentors': 'mentor',
                    'description2': 'responsibilities',
                    'keyword_abstract': 'rkeywords',
                    'techniques': 'techniques',
                    'instruments': 'instruments',
                    'softwares': 'softwares',
                    'soft_skills': 'softskills',
                    'description': 'skilldesc',
                    'keyword_description': 'skeywords'
                }

                # Loop over the fields and prepare SQL update statement
                for form_field, db_info in form_to_db_map.items():
                    # db_info can be either a string or a tuple (column_name, transform_function)
                    db_column, transform = db_info if isinstance(db_info, tuple) else (db_info, None)
                    form_data = get_form_data_or_none(form_field)
                    if form_data is not None:
                        updates.append(f"{db_column} = %s")
                        # Apply transformation function if provided
                        values.append(transform(form_data) if transform else form_data)
                print("_________________STEP 1__________________")
                if updates:
                    update_sql = ", ".join(updates)
                    sql = f"UPDATE gvolunteer SET {update_sql} WHERE id = %s"
                    values.append(experience_id)
                    print(update_sql)
                    print(experience_id)
                    print(sql)
                    mycursor = sqlconnection.cursor()
                    mycursor.execute(sql, tuple(values))
                    sqlconnection.commit()
                    mycursor.close()
                    print("_________________STEP 2 EDIT__________________")
                    flash('Experience updated successfully!', 'success')
                else:
                    flash('No changes to update.', 'info')

            except Exception as e:
                flash('Failed to update experience due to an error.', 'error')
                print(f"Error updating experience: {e}")
                return render_template('error_template.html'), 500
            ## Code to Read
            documents = volunteer_read_table(user)
            return render_template('grantize/profile/volunteer.html', documents = documents)
        if "permissions" in request.form:
            try:
                if request.form.get("public"):
                    except_persons = request.form['except_persons']
                    prmission_show_me('gcredentials',except_persons, user)
                if request.form.get("designation"):
                    except_persons = request.form.getlist('designations')
                    prmission_hide_designation('gcredentials', except_persons, user)
                if request.form.get("person"):
                    except_persons = request.form['except_invidividuals']
                    prmission_hide_individuals('gcredentials', except_persons, user)
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/volunteer.html')
            try:
                mycursor = sqlconnection.cursor()
                sql = "INSERT INTO gvolunteer (userid, description, organization, filename, filecontent) VALUES (%s, %s, %s, %s, %s)"
                values = (user, credname, credorg, credfilename, file_content)
                mycursor.execute(sql, values)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("DATBASE FAILURE!!")
                return render_template('grantize/profile/volunteer.html')
            ## Code to Read
            documents = volunteer_read_table(user)
            return render_template('grantize/profile/volunteer.html', documents=documents)
        if "delete" in request.form:
            try:
                id_to_delete = request.form['id']
                print("-------------")
                print(id_to_delete)
                print("--------------")
                mycursor = sqlconnection.cursor()
                sql = "DELETE FROM gvolunteer WHERE id = "+str(id_to_delete)
                mycursor.execute(sql)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/volunteer.html')
            ## Code to Read
            documents = volunteer_read_table(user)
            return render_template('grantize/profile/volunteer.html', documents = documents)
        else:
            documents = volunteer_read_table(user)
            print(documents)
            return render_template('grantize/profile/volunteer.html', documents = documents)
    else:
        return render_template('grantize/grantize.html')
    
def awards_read_table(user):
    global sqlconnection
    try:
        mycursor = sqlconnection.cursor(dictionary=True)
        # SQL query to get all columns except 'id' and 'userid' from gawards
        query = """
        SELECT id, awards, type, vdate, organization, department, description
        FROM gawards
        WHERE userid = %s
        """
        mycursor.execute(query, (user,))
        rows = mycursor.fetchall()
        
        # Convert rows to a list of dictionaries for easy handling in the template
        awards = []
        for row in rows:
            awards.append(row)
            
        mycursor.close()
        return awards
    except Exception as e:
        print("Error fetching awards from database:", str(e))
        return []
    
@app.route('/grantizeprofileawards', methods =["GET", "POST"])
def grantizeprofileawards():
    global sqlconnection
    if session.get("loginnname"):
        user = session.get('loginid')
        if "createawards" in request.form:
            try:
                # Helper function to get the form data or return None if blank
                def get_form_data_or_none(field_name):
                    return request.form[field_name] if field_name in request.form and request.form[field_name].strip() else None
                # Retrieve form data
                awards = get_form_data_or_none('awards')  # Assuming you populate this select in your form
                award_type = get_form_data_or_none('type')
                award_date = get_form_data_or_none('vdate')
                award_organization = get_form_data_or_none('organization')
                award_department = get_form_data_or_none('department')
                award_description = get_form_data_or_none('description')
                keywords = ','.join(request.form.getlist('keyword_description'))  # Convert list of keywords into a string
                # Convert date from string to date object
                award_date = datetime.strptime(award_date, '%m-%d-%Y').date() if award_date else None
            except Exception as e:
                print(f"Error reading form data: {str(e)}")
                return render_template('grantize/profile/awards.html')
            try:
                cursor = sqlconnection.cursor()
                sql = """
                INSERT INTO gawards (userid, awards, type, vdate, organization, department, description, keywords)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (user, awards, award_type, award_date, award_organization, award_department, award_description, keywords)  # Example with user ID as 1
                cursor.execute(sql, values)
                sqlconnection.commit()
                flash('Award added successfully!', 'success')
            except Exception as e:
                print(f"Database Error: {str(e)}")
                sqlconnection.rollback()
                flash('Failed to add award.', 'error')
                return render_template('grantize/profile/awards.html', error="Failed to add award.")
            finally:
                if sqlconnection.is_connected():
                    cursor.close()
            ## Code to Read
            documents = awards_read_table(user)
            return render_template('grantize/profile/awards.html', documents = documents)
        if "editsection" in request.form:
            try:
                print("_________________EDIT STEP 0__________________")
                award_id = request.form['award_id']  # Ensure you have an input in your form with name='award_id'
                updates = []
                values = []

                # Helper function to get form data or None
                def get_form_data_or_none(field):
                    return request.form[field].strip() if field in request.form and request.form[field].strip() else None

                # Define the mapping from form fields to database columns
                form_to_db_map = {
                    'awards': 'awards',
                    'type': 'type',
                    'vdate': ('vdate', lambda x: datetime.strptime(x, '%m-%d-%Y').strftime('%Y-%m-%d') if x else None),
                    'organization': 'organization',
                    'department': 'department',
                    'description': 'description',
                    'keyword_description': 'keywords'
                }

                # Loop over the fields and prepare SQL update statement
                for form_field, db_info in form_to_db_map.items():
                    db_column, transform = db_info if isinstance(db_info, tuple) else (db_info, None)
                    form_data = get_form_data_or_none(form_field)
                    if form_data is not None:
                        updates.append(f"{db_column} = %s")
                        # Apply transformation function if provided
                        values.append(transform(form_data) if transform else form_data)

                print("_________________EDIT STEP 1__________________")

                if updates:
                    update_sql = ", ".join(updates)
                    sql = f"UPDATE gawards SET {update_sql} WHERE id = %s"
                    print(sql)
                    print(values)
                    values.append(award_id)
                    print(award_id)
                    mycursor = sqlconnection.cursor()
                    mycursor.execute(sql, tuple(values))
                    sqlconnection.commit()
                    mycursor.close()
                    flash('Award updated successfully!', 'success')
                else:
                    flash('No changes to update.', 'info')

                print("_________________EDIT STEP 2__________________")

            except Exception as e:
                flash(f'Failed to update award due to an error: {e}', 'error')
                return render_template('error_template.html'), 500
            ## Code to Read updated data
            documents = awards_read_table(user)
            return render_template('grantize/profile/awards.html', documents=documents)
        if "permissions" in request.form:
            try:
                if request.form.get("public"):
                    except_persons = request.form['except_persons']
                    prmission_show_me('gcredentials',except_persons, user)
                if request.form.get("designation"):
                    except_persons = request.form.getlist('designations')
                    prmission_hide_designation('gcredentials', except_persons, user)
                if request.form.get("person"):
                    except_persons = request.form['except_invidividuals']
                    prmission_hide_individuals('gcredentials', except_persons, user)
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/awards.html')
            try:
                mycursor = sqlconnection.cursor()
                sql = "INSERT INTO gvolunteer (userid, description, organization, filename, filecontent) VALUES (%s, %s, %s, %s, %s)"
                values = (user, credname, credorg, credfilename, file_content)
                mycursor.execute(sql, values)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("DATBASE FAILURE!!")
                return render_template('grantize/profile/awards.html')
            ## Code to Read
            documents = awards_read_table(user)
            return render_template('grantize/profile/awards.html', documents=documents)
        if "delete" in request.form:
            try:
                id_to_delete = request.form['id']
                print("-------------")
                print(id_to_delete)
                print("--------------")
                mycursor = sqlconnection.cursor()
                sql = "DELETE FROM gawards WHERE id = "+str(id_to_delete)
                mycursor.execute(sql)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/awards.html')
            ## Code to Read
            documents = awards_read_table(user)
            return render_template('grantize/profile/awards.html', documents = documents)
        else:
            documents = awards_read_table(user)
            print(documents)
            return render_template('grantize/profile/awards.html', documents = documents)
    else:
        return render_template('grantize/grantize.html')
    
def grants_read_table(user):
    global sqlconnection
    try:
        mycursor = sqlconnection.cursor(dictionary=True)
        # SQL query to get all columns except 'id' and 'userid' from ggrants
        query = """
        SELECT id, title, project_number, total_funding, url, start_date, end_date, principal_investigators,
               investigators, funding_org, funding_dept, awardee_org, awardee_dept, project_terms, 
               abstract, abstract_keywords
        FROM ggrantscontracts
        WHERE userid = %s
        """
        mycursor.execute(query, (user,))
        rows = mycursor.fetchall()
        
        # Convert rows to a list of dictionaries for easy handling in the template
        grants = []
        for row in rows:
            grants.append(row)
            
        mycursor.close()
        return grants
    except Exception as e:
        print("Error fetching grants from database:", str(e))
        return []

@app.route('/grantizeprofilegrantscontracts', methods =["GET", "POST"])
def grantizeprofilegrantscontracts():
    global sqlconnection
    if session.get("loginnname"):
        user = session.get('loginid')
        if "creategrant" in request.form:
            try:
                # Helper function to retrieve form data or None if the field is empty
                def get_form_data_or_none(field_name):
                    return request.form[field_name] if field_name in request.form and request.form[field_name].strip() else None

                # Extract form data
                title = get_form_data_or_none('title')
                project_number = get_form_data_or_none('name')
                total_funding = get_form_data_or_none('type')
                url = get_form_data_or_none('url')
                start_date = get_form_data_or_none('start_date')
                end_date = get_form_data_or_none('end_date')
                principal_investigators = get_form_data_or_none('authors')
                investigators = get_form_data_or_none('co_authors')
                funding_org = get_form_data_or_none('sponsor')
                funding_dept = get_form_data_or_none('sponsor_department')
                awardee_org = get_form_data_or_none('organization')
                awardee_dept = get_form_data_or_none('department')
                project_terms = request.form.getlist('keywords')  # Handle multiple select inputs
                abstract = get_form_data_or_none('description')
                abstract_keywords = get_form_data_or_none('keyword_abstract')

                # Format dates
                if start_date:
                    start_date = datetime.strptime(start_date, '%m-%d-%Y').date()
                if end_date:
                    end_date = datetime.strptime(end_date, '%m-%d-%Y').date()

                # Prepare SQL query and data
                sql = """
                INSERT INTO ggrantscontracts
                (userid, title, project_number, total_funding, url, start_date, end_date, 
                principal_investigators, investigators, funding_org, funding_dept, 
                awardee_org, awardee_dept, project_terms, abstract, abstract_keywords)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = [user, title, project_number, total_funding, url, start_date, end_date, 
                        principal_investigators, investigators, funding_org, funding_dept, 
                        awardee_org, awardee_dept, ','.join(project_terms), abstract, abstract_keywords]
                for i in range(len(values)):
                    if values[i] == None:
                        values[i] = ""
                # Execute the query
                mycursor = sqlconnection.cursor()
                mycursor.execute(sql, tuple(values))
                sqlconnection.commit()
                mycursor.close()
                flash('Grant contract added successfully!', 'success')
            except Exception as e:
                flash(f'Failed to add grant contract due to an error: {str(e)}', 'error')
                return render_template('error_template.html'), 500
            documents = grants_read_table(user)
            return render_template('grantize/profile/grantscontracts.html', documents = documents)
        if "editsection" in request.form:
            try:
                print("_________________EDIT STEP 0__________________")
                grant_id = request.form['grant_id']  # Ensure you have a hidden input in your form with the name 'document_id'
                updates = []
                values = []

                # Helper function to get form data or return None if blank
                def get_form_data_or_none(field):
                    return request.form[field].strip() if field in request.form and request.form[field].strip() else None

                # Define the mapping from form fields to database columns
                form_to_db_map = {
                    'title': 'title',
                    'name': 'project_number',
                    'type': 'total_funding',
                    'url': 'url',
                    'start_date': ('start_date', lambda x: datetime.strptime(x, '%m-%d-%Y').strftime('%Y-%m-%d') if x else None),
                    'end_date': ('end_date', lambda x: datetime.strptime(x, '%m-%d-%Y').strftime('%Y-%m-%d') if x else None),
                    'authors': 'principal_investigators',
                    'co_authors': 'investigators',
                    'sponsor': 'funding_org',
                    'sponsor_department': '	funding_dept',
                    'organization': 'awardee_org',
                    'department': 'awardee_dept',
                    'keywords': 'project_terms',
                    'abstract': 'abstract',
                    'keyword_abstract': 'abstract_keywords'
                }

                # Loop over the fields and prepare SQL update statement
                for form_field, db_info in form_to_db_map.items():
                    db_column, transform = db_info if isinstance(db_info, tuple) else (db_info, None)
                    form_data = get_form_data_or_none(form_field)
                    if form_data is not None:
                        updates.append(f"{db_column} = %s")
                        # Apply transformation function if provided
                        values.append(transform(form_data) if transform else form_data)

                print("_________________EDIT STEP 1__________________")

                if updates:
                    update_sql = ", ".join(updates)
                    sql = f"UPDATE ggrantscontracts SET {update_sql} WHERE id = %s"
                    print(sql)
                    values.append(grant_id)
                    print(values)
                    mycursor = sqlconnection.cursor()
                    mycursor.execute(sql, tuple(values))
                    sqlconnection.commit()
                    mycursor.close()
                    flash('Grant details updated successfully!', 'success')
                else:
                    flash('No changes to update.', 'info')

                print("_________________EDIT STEP 2__________________")

            except Exception as e:
                flash(f'Failed to update grant details due to an error: {e}', 'error')
                return render_template('error_template.html'), 500
            documents = grants_read_table(user)
            return render_template('grantize/profile/grantscontracts.html', documents = documents)
        if "delete" in request.form:
            try:
                id_to_delete = request.form['id']
                print("-------------")
                print(id_to_delete)
                print("--------------")
                mycursor = sqlconnection.cursor()
                sql = "DELETE FROM ggrantscontracts WHERE id = "+str(id_to_delete)
                mycursor.execute(sql)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/grantscontracts.html')
            ## Code to Read
            documents = grants_read_table(user)
            return render_template('grantize/profile/grantscontracts.html', documents = documents)
        else:
            documents = grants_read_table(user)
            return render_template('grantize/profile/grantscontracts.html', documents = documents)
    else:
        return render_template('grantize/grantize.html')
    
def patents_read_table(user):
    global sqlconnection
    try:
        mycursor = sqlconnection.cursor(dictionary=True)
        # SQL query to get all columns except 'id' and 'userid' from ggrants
        query = """
        SELECT id, title, project_number, total_funding, url, start_date, end_date, principal_investigators,
               investigators, funding_org, funding_dept, awardee_org, awardee_dept, project_terms, 
               abstract, abstract_keywords
        FROM gpatents
        WHERE userid = %s
        """
        mycursor.execute(query, (user,))
        rows = mycursor.fetchall()
        
        # Convert rows to a list of dictionaries for easy handling in the template
        grants = []
        for row in rows:
            grants.append(row)
            
        mycursor.close()
        return grants
    except Exception as e:
        print("Error fetching grants from database:", str(e))
        return []

@app.route('/grantizeprofilepatents', methods =["GET", "POST"])
def grantizeprofilepatents():
    if session.get("loginnname"):
        user = session.get('loginid')
        if "creategrant" in request.form:
            try:
                # Helper function to retrieve form data or None if the field is empty
                def get_form_data_or_none(field_name):
                    return request.form[field_name] if field_name in request.form and request.form[field_name].strip() else None

                # Extract form data
                title = get_form_data_or_none('title')
                project_number = get_form_data_or_none('name')
                total_funding = get_form_data_or_none('type')
                url = get_form_data_or_none('url')
                start_date = get_form_data_or_none('start_date')
                end_date = get_form_data_or_none('end_date')
                principal_investigators = get_form_data_or_none('authors')
                investigators = get_form_data_or_none('co_authors')
                funding_org = get_form_data_or_none('sponsor')
                funding_dept = get_form_data_or_none('sponsor_department')
                awardee_org = get_form_data_or_none('organization')
                awardee_dept = get_form_data_or_none('department')
                project_terms = request.form.getlist('keywords')  # Handle multiple select inputs
                abstract = get_form_data_or_none('description')
                abstract_keywords = get_form_data_or_none('keyword_abstract')

                # Format dates
                if start_date:
                    start_date = datetime.strptime(start_date, '%m-%d-%Y').date()
                if end_date:
                    end_date = datetime.strptime(end_date, '%m-%d-%Y').date()

                # Prepare SQL query and data
                sql = """
                INSERT INTO gpatents
                (userid, title, project_number, total_funding, url, start_date, end_date, 
                principal_investigators, investigators, funding_org, funding_dept, 
                awardee_org, awardee_dept, project_terms, abstract, abstract_keywords)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = [user, title, project_number, total_funding, url, start_date, end_date, 
                        principal_investigators, investigators, funding_org, funding_dept, 
                        awardee_org, awardee_dept, ','.join(project_terms), abstract, abstract_keywords]
                for i in range(len(values)):
                    if values[i] == None:
                        values[i] = ""
                # Execute the query
                mycursor = sqlconnection.cursor()
                mycursor.execute(sql, tuple(values))
                sqlconnection.commit()
                mycursor.close()
                flash('Grant contract added successfully!', 'success')
            except Exception as e:
                flash(f'Failed to add grant contract due to an error: {str(e)}', 'error')
                return render_template('error_template.html'), 500
            documents = patents_read_table(user)
            return render_template('grantize/profile/patents.html', documents = documents)
        if "editsection" in request.form:
            try:
                print("_________________EDIT STEP 0__________________")
                grant_id = request.form['grant_id']  # Ensure you have a hidden input in your form with the name 'document_id'
                updates = []
                values = []

                # Helper function to get form data or return None if blank
                def get_form_data_or_none(field):
                    return request.form[field].strip() if field in request.form and request.form[field].strip() else None

                # Define the mapping from form fields to database columns
                form_to_db_map = {
                    'title': 'title',
                    'name': 'project_number',
                    'type': 'total_funding',
                    'url': 'url',
                    'start_date': ('start_date', lambda x: datetime.strptime(x, '%m-%d-%Y').strftime('%Y-%m-%d') if x else None),
                    'end_date': ('end_date', lambda x: datetime.strptime(x, '%m-%d-%Y').strftime('%Y-%m-%d') if x else None),
                    'authors': 'principal_investigators',
                    'co_authors': 'investigators',
                    'sponsor': 'funding_org',
                    'sponsor_department': '	funding_dept',
                    'organization': 'awardee_org',
                    'department': 'awardee_dept',
                    'keywords': 'project_terms',
                    'abstract': 'abstract',
                    'keyword_abstract': 'abstract_keywords'
                }

                # Loop over the fields and prepare SQL update statement
                for form_field, db_info in form_to_db_map.items():
                    db_column, transform = db_info if isinstance(db_info, tuple) else (db_info, None)
                    form_data = get_form_data_or_none(form_field)
                    if form_data is not None:
                        updates.append(f"{db_column} = %s")
                        # Apply transformation function if provided
                        values.append(transform(form_data) if transform else form_data)

                print("_________________EDIT STEP 1__________________")

                if updates:
                    update_sql = ", ".join(updates)
                    sql = f"UPDATE gpatents SET {update_sql} WHERE id = %s"
                    print(sql)
                    values.append(grant_id)
                    print(values)
                    mycursor = sqlconnection.cursor()
                    mycursor.execute(sql, tuple(values))
                    sqlconnection.commit()
                    mycursor.close()
                    flash('Grant details updated successfully!', 'success')
                else:
                    flash('No changes to update.', 'info')

                print("_________________EDIT STEP 2__________________")

            except Exception as e:
                flash(f'Failed to update grant details due to an error: {e}', 'error')
                return render_template('error_template.html'), 500
            documents = patents_read_table(user)
            return render_template('grantize/profile/patents.html', documents = documents)
        if "delete" in request.form:
            try:
                id_to_delete = request.form['id']
                print("-------------")
                print(id_to_delete)
                print("--------------")
                mycursor = sqlconnection.cursor()
                sql = "DELETE FROM gpatents WHERE id = "+str(id_to_delete)
                mycursor.execute(sql)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/patents.html')
            ## Code to Read
            documents = patents_read_table(user)
            return render_template('grantize/profile/patents.html', documents = documents)
        else:
            documents = patents_read_table(user)
            return render_template('grantize/profile/patents.html', documents = documents)
    else:
        return render_template('grantize/grantize.html')
    
def journalres_read_table(user):
    global sqlconnection
    try:
        mycursor = sqlconnection.cursor(dictionary=True)
        # SQL query to get specific columns from the journals table that are used in the INSERT query
        query = """
        SELECT id, publication_status, publisher, journal, year, volume, issue, page, title, url, doi,
               organization, department, authors, co_authors, corresponding_authors, keywords,
               abstract, abstract_keywords, techniques, instruments, softwares, soft_skills
        FROM gjournals
        WHERE userid = %s
        """
        mycursor.execute(query, (user,))
        rows = mycursor.fetchall()
        
        # Convert rows to a list of dictionaries to facilitate handling in the template
        documents = []
        for row in rows:
            documents.append(row)
        
        mycursor.close()
        return documents
    except Exception as e:
        print("Error fetching documents from database:", str(e))
        return []



@app.route('/grantizeprofilejourorgres', methods =["GET", "POST"])
def grantizeprofilejourorgres():
    if session.get("loginnname"):
        user = session.get('loginid')
        if "createjourres" in request.form:
            print("_________________CREATE STEP 0__________________")
            try:
                # Helper function to retrieve form data or None if the field is empty
                def get_form_data_or_none(field_name):
                    return request.form[field_name] if field_name in request.form and request.form[field_name].strip() else None

                # Extract form data
                publication_status = get_form_data_or_none('publication_status')
                publisher = get_form_data_or_none('publisher')
                journal = get_form_data_or_none('journal')
                year = get_form_data_or_none('year')
                volume = get_form_data_or_none('volume')
                issue = get_form_data_or_none('issue')
                page = get_form_data_or_none('page')
                title = get_form_data_or_none('title')
                url = get_form_data_or_none('url')
                doi = get_form_data_or_none('doi')
                organization = get_form_data_or_none('organization')
                department = get_form_data_or_none('department')
                authors = get_form_data_or_none('authors')
                co_authors = get_form_data_or_none('co_authors')
                corresponding_authors = get_form_data_or_none('corresponding_authors')
                keywords = get_form_data_or_none('keywords')
                abstract = get_form_data_or_none('abstract')
                abstract_keywords = get_form_data_or_none('keyword_abstract')
                techniques = get_form_data_or_none('techniques')
                instruments = get_form_data_or_none('instruments')
                softwares = get_form_data_or_none('softwares')
                soft_skills = get_form_data_or_none('soft_skills')

                print("_________________CREATE STEP 1__________________")
                # Prepare SQL query and data
                sql = """
                INSERT INTO gjournals
                (userid, publication_status, publisher, journal, year, volume, issue, page, title, url, doi, organization, 
                department, authors, co_authors, corresponding_authors, keywords, abstract, abstract_keywords, 
                techniques, instruments, softwares, soft_skills)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = [user, publication_status, publisher, journal, year, volume, issue, page, title, url, doi, organization, 
                        department, authors, co_authors, corresponding_authors, keywords, abstract, abstract_keywords, 
                        techniques, instruments, softwares, soft_skills]
                
                # Convert None values to empty strings before executing
                values = ["" if v is None else v for v in values]
                print(values)
                # Execute the query
                mycursor = sqlconnection.cursor()
                mycursor.execute(sql, tuple(values))
                sqlconnection.commit()
                mycursor.close()
                flash('Journal information added successfully!', 'success')
                print("_________________CREATE STEP 2__________________")
            except Exception as e:
                flash(f'Failed to add journal information due to an error: {str(e)}', 'error')
                return render_template('error_template.html'), 500
            documents = journalres_read_table(user)
            return render_template('grantize/profile/journalresearch.html', documents=documents)
        if "editsection" in request.form:
            print("_________________EDIT STEP 0__________________")
            try:
                journal_id = request.form['journal_id']
                updates = []
                values = []

                # Helper function to get form data or return None if blank
                def get_form_data_or_none(field):
                    return request.form[field].strip() if field in request.form and request.form[field].strip() else None

                # Define the mapping from form fields to database columns
                form_to_db_map = {
                    'publication_status': 'publication_status',
                    'publisher': 'publisher',
                    'journal': 'journal',
                    'year': 'year',
                    'volume': 'volume',
                    'issue': 'issue',
                    'page': 'page',
                    'title': 'title',
                    'url': 'url',
                    'doi': 'doi',
                    'organization': 'organization',
                    'department': 'department',
                    'authors': 'authors',
                    'co_authors': 'co_authors',
                    'corresponding_authors': 'corresponding_authors',
                    'keywords': 'keywords',
                    'abstract': 'abstract',
                    'abstract_keywords': 'abstract_keywords',
                    'techniques': 'techniques',
                    'instruments': 'instruments',
                    'softwares': 'softwares',
                    'soft_skills': 'soft_skills'
                }

                # Loop over the fields and prepare SQL update statement
                for form_field, db_column in form_to_db_map.items():
                    form_data = get_form_data_or_none(form_field)
                    if form_data is not None:
                        updates.append(f"{db_column} = %s")
                        values.append(form_data)

                print("_________________EDIT STEP 1__________________")

                # Check if there are any updates to be made
                if updates:
                    update_sql = ", ".join(updates)
                    print("_________________EDIT STEP 2__________________")
                    sql = f"UPDATE gjournals SET {update_sql} WHERE id = %s"
                    print(sql)
                    values.append(journal_id)
                    mycursor = sqlconnection.cursor()
                    print(values)
                    mycursor.execute(sql, tuple(values))
                    sqlconnection.commit()
                    mycursor.close()
                    print("_________________EDIT STEP 3__________________")
                    flash('Journal details updated successfully!', 'success')
                else:
                    flash('No changes to update.', 'info')
            except Exception as e:
                flash(f'Failed to update journal details due to an error: {str(e)}', 'error')
                return render_template('error_template.html'), 500
            documents = journalres_read_table(user)
            return render_template('grantize/profile/journalresearch.html', documents=documents)
        if "delete" in request.form:
            try:
                id_to_delete = request.form['id']
                print("-------------")
                print(id_to_delete)
                print("--------------")
                mycursor = sqlconnection.cursor()
                sql = "DELETE FROM gjournals WHERE id = "+str(id_to_delete)
                mycursor.execute(sql)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/journalresearch.html')
            ## Code to Read
            documents = journalres_read_table(user)
            return render_template('grantize/profile/journalresearch.html', documents = documents)
        else:
            documents = journalres_read_table(user)
            print(documents)
            return render_template('grantize/profile/journalresearch.html', documents=documents)
    else:
        return render_template('grantize/grantize.html')

def shorts_read_table(user):
    global sqlconnection
    try:
        mycursor = sqlconnection.cursor(dictionary=True)
        # SQL query to get specific columns from the journals table that are used in the INSERT query
        query = """
        SELECT id, publication_status, publisher, journal, year, volume, issue, page, title, url, doi,
               organization, department, authors, co_authors, corresponding_authors, keywords,
               abstract, abstract_keywords, techniques, instruments, softwares, soft_skills
        FROM gshorts
        WHERE userid = %s
        """
        mycursor.execute(query, (user,))
        rows = mycursor.fetchall()
        
        # Convert rows to a list of dictionaries to facilitate handling in the template
        documents = []
        for row in rows:
            documents.append(row)
        
        mycursor.close()
        return documents
    except Exception as e:
        print("Error fetching documents from database:", str(e))
        return []

@app.route('/grantizeprofilejourshortsrep', methods =["GET", "POST"])
def grantizeprofilejourshortsrep():
    if session.get("loginnname"):
        user = session.get('loginid')
        if "createjourshorts" in request.form:
            print("_________________CREATE STEP 0__________________")
            try:
                # Helper function to retrieve form data or None if the field is empty
                def get_form_data_or_none(field_name):
                    return request.form[field_name] if field_name in request.form and request.form[field_name].strip() else None

                # Extract form data
                publication_status = get_form_data_or_none('publication_status')
                publisher = get_form_data_or_none('publisher')
                journal = get_form_data_or_none('journal')
                year = get_form_data_or_none('year')
                volume = get_form_data_or_none('volume')
                issue = get_form_data_or_none('issue')
                page = get_form_data_or_none('page')
                title = get_form_data_or_none('title')
                url = get_form_data_or_none('url')
                doi = get_form_data_or_none('doi')
                organization = get_form_data_or_none('organization')
                department = get_form_data_or_none('department')
                authors = get_form_data_or_none('authors')
                co_authors = get_form_data_or_none('co_authors')
                corresponding_authors = get_form_data_or_none('corresponding_authors')
                keywords = get_form_data_or_none('keywords')
                abstract = get_form_data_or_none('abstract')
                abstract_keywords = get_form_data_or_none('keyword_abstract')
                techniques = get_form_data_or_none('techniques')
                instruments = get_form_data_or_none('instruments')
                softwares = get_form_data_or_none('softwares')
                soft_skills = get_form_data_or_none('soft_skills')

                print("_________________CREATE STEP 1__________________")
                # Prepare SQL query and data
                sql = """
                INSERT INTO gshorts
                (userid, publication_status, publisher, journal, year, volume, issue, page, title, url, doi, organization, 
                department, authors, co_authors, corresponding_authors, keywords, abstract, abstract_keywords, 
                techniques, instruments, softwares, soft_skills)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = [user, publication_status, publisher, journal, year, volume, issue, page, title, url, doi, organization, 
                        department, authors, co_authors, corresponding_authors, keywords, abstract, abstract_keywords, 
                        techniques, instruments, softwares, soft_skills]
                
                # Convert None values to empty strings before executing
                values = ["" if v is None else v for v in values]
                print(values)
                # Execute the query
                mycursor = sqlconnection.cursor()
                mycursor.execute(sql, tuple(values))
                sqlconnection.commit()
                mycursor.close()
                flash('Journal information added successfully!', 'success')
                print("_________________CREATE STEP 2__________________")
            except Exception as e:
                flash(f'Failed to add journal information due to an error: {str(e)}', 'error')
                return render_template('error_template.html'), 500
            documents = shorts_read_table(user)
            return render_template('grantize/profile/journalshortreport.html', documents=documents)
        if "editsection" in request.form:
            print("_________________EDIT STEP 0__________________")
            try:
                journal_id = request.form['journal_id']
                updates = []
                values = []

                # Helper function to get form data or return None if blank
                def get_form_data_or_none(field):
                    return request.form[field].strip() if field in request.form and request.form[field].strip() else None

                # Define the mapping from form fields to database columns
                form_to_db_map = {
                    'publication_status': 'publication_status',
                    'publisher': 'publisher',
                    'journal': 'journal',
                    'year': 'year',
                    'volume': 'volume',
                    'issue': 'issue',
                    'page': 'page',
                    'title': 'title',
                    'url': 'url',
                    'doi': 'doi',
                    'organization': 'organization',
                    'department': 'department',
                    'authors': 'authors',
                    'co_authors': 'co_authors',
                    'corresponding_authors': 'corresponding_authors',
                    'keywords': 'keywords',
                    'abstract': 'abstract',
                    'abstract_keywords': 'abstract_keywords',
                    'techniques': 'techniques',
                    'instruments': 'instruments',
                    'softwares': 'softwares',
                    'soft_skills': 'soft_skills'
                }

                # Loop over the fields and prepare SQL update statement
                for form_field, db_column in form_to_db_map.items():
                    form_data = get_form_data_or_none(form_field)
                    if form_data is not None:
                        updates.append(f"{db_column} = %s")
                        values.append(form_data)

                print("_________________EDIT STEP 1__________________")

                # Check if there are any updates to be made
                if updates:
                    update_sql = ", ".join(updates)
                    print("_________________EDIT STEP 2__________________")
                    sql = f"UPDATE gshorts SET {update_sql} WHERE id = %s"
                    print(sql)
                    values.append(journal_id)
                    mycursor = sqlconnection.cursor()
                    print(values)
                    mycursor.execute(sql, tuple(values))
                    sqlconnection.commit()
                    mycursor.close()
                    print("_________________EDIT STEP 3__________________")
                    flash('Journal details updated successfully!', 'success')
                else:
                    flash('No changes to update.', 'info')
            except Exception as e:
                flash(f'Failed to update journal details due to an error: {str(e)}', 'error')
                return render_template('error_template.html'), 500
            documents = shorts_read_table(user)
            return render_template('grantize/profile/journalshortreport.html', documents=documents)
        if "delete" in request.form:
            try:
                id_to_delete = request.form['id']
                print("-------------")
                print(id_to_delete)
                print("--------------")
                mycursor = sqlconnection.cursor()
                sql = "DELETE FROM gshorts WHERE id = "+str(id_to_delete)
                mycursor.execute(sql)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/journalshortreport.html')
            ## Code to Read
            documents = shorts_read_table(user)
            return render_template('grantize/profile/journalshortreport.html', documents = documents)
        else:
            documents = shorts_read_table(user)
            print(documents)
            return render_template('grantize/profile/journalshortreport.html', documents=documents)
    else:
        return render_template('grantize/grantize.html')

def articles_read_table(user):
    global sqlconnection
    try:
        mycursor = sqlconnection.cursor(dictionary=True)
        # SQL query to get specific columns from the journals table that are used in the INSERT query
        query = """
        SELECT id, publication_status, publisher, journal, year, volume, issue, page, title, url, doi,
               organization, department, authors, co_authors, corresponding_authors, keywords,
               abstract, abstract_keywords, techniques, instruments, softwares, soft_skills
        FROM garticles
        WHERE userid = %s
        """
        mycursor.execute(query, (user,))
        rows = mycursor.fetchall()
        
        # Convert rows to a list of dictionaries to facilitate handling in the template
        documents = []
        for row in rows:
            documents.append(row)
        
        mycursor.close()
        return documents
    except Exception as e:
        print("Error fetching documents from database:", str(e))
        return []  

@app.route('/grantizeprofilejourreviewarts', methods =["GET", "POST"])
def grantizeprofilejourreviewarts():
    if session.get("loginnname"):
        user = session.get('loginid')
        if "createjourshorts" in request.form:
            print("_________________CREATE STEP 0__________________")
            try:
                # Helper function to retrieve form data or None if the field is empty
                def get_form_data_or_none(field_name):
                    return request.form[field_name] if field_name in request.form and request.form[field_name].strip() else None

                # Extract form data
                publication_status = get_form_data_or_none('publication_status')
                publisher = get_form_data_or_none('publisher')
                journal = get_form_data_or_none('journal')
                year = get_form_data_or_none('year')
                volume = get_form_data_or_none('volume')
                issue = get_form_data_or_none('issue')
                page = get_form_data_or_none('page')
                title = get_form_data_or_none('title')
                url = get_form_data_or_none('url')
                doi = get_form_data_or_none('doi')
                organization = get_form_data_or_none('organization')
                department = get_form_data_or_none('department')
                authors = get_form_data_or_none('authors')
                co_authors = get_form_data_or_none('co_authors')
                corresponding_authors = get_form_data_or_none('corresponding_authors')
                keywords = get_form_data_or_none('keywords')
                abstract = get_form_data_or_none('abstract')
                abstract_keywords = get_form_data_or_none('keyword_abstract')
                techniques = get_form_data_or_none('techniques')
                instruments = get_form_data_or_none('instruments')
                softwares = get_form_data_or_none('softwares')
                soft_skills = get_form_data_or_none('soft_skills')

                print("_________________CREATE STEP 1__________________")
                # Prepare SQL query and data
                sql = """
                INSERT INTO garticles
                (userid, publication_status, publisher, journal, year, volume, issue, page, title, url, doi, organization, 
                department, authors, co_authors, corresponding_authors, keywords, abstract, abstract_keywords, 
                techniques, instruments, softwares, soft_skills)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = [user, publication_status, publisher, journal, year, volume, issue, page, title, url, doi, organization, 
                        department, authors, co_authors, corresponding_authors, keywords, abstract, abstract_keywords, 
                        techniques, instruments, softwares, soft_skills]
                
                # Convert None values to empty strings before executing
                values = ["" if v is None else v for v in values]
                print(values)
                # Execute the query
                mycursor = sqlconnection.cursor()
                mycursor.execute(sql, tuple(values))
                sqlconnection.commit()
                mycursor.close()
                flash('Journal information added successfully!', 'success')
                print("_________________CREATE STEP 2__________________")
            except Exception as e:
                flash(f'Failed to add journal information due to an error: {str(e)}', 'error')
                return render_template('error_template.html'), 500
            documents = articles_read_table(user)
            return render_template('grantize/profile/journalreviewarticles.html', documents=documents)
        if "editsection" in request.form:
            print("_________________EDIT STEP 0__________________")
            try:
                journal_id = request.form['journal_id']
                updates = []
                values = []

                # Helper function to get form data or return None if blank
                def get_form_data_or_none(field):
                    return request.form[field].strip() if field in request.form and request.form[field].strip() else None

                # Define the mapping from form fields to database columns
                form_to_db_map = {
                    'publication_status': 'publication_status',
                    'publisher': 'publisher',
                    'journal': 'journal',
                    'year': 'year',
                    'volume': 'volume',
                    'issue': 'issue',
                    'page': 'page',
                    'title': 'title',
                    'url': 'url',
                    'doi': 'doi',
                    'organization': 'organization',
                    'department': 'department',
                    'authors': 'authors',
                    'co_authors': 'co_authors',
                    'corresponding_authors': 'corresponding_authors',
                    'keywords': 'keywords',
                    'abstract': 'abstract',
                    'abstract_keywords': 'abstract_keywords',
                    'techniques': 'techniques',
                    'instruments': 'instruments',
                    'softwares': 'softwares',
                    'soft_skills': 'soft_skills'
                }

                # Loop over the fields and prepare SQL update statement
                for form_field, db_column in form_to_db_map.items():
                    form_data = get_form_data_or_none(form_field)
                    if form_data is not None:
                        updates.append(f"{db_column} = %s")
                        values.append(form_data)

                print("_________________EDIT STEP 1__________________")

                # Check if there are any updates to be made
                if updates:
                    update_sql = ", ".join(updates)
                    print("_________________EDIT STEP 2__________________")
                    sql = f"UPDATE garticles SET {update_sql} WHERE id = %s"
                    print(sql)
                    values.append(journal_id)
                    mycursor = sqlconnection.cursor()
                    print(values)
                    mycursor.execute(sql, tuple(values))
                    sqlconnection.commit()
                    mycursor.close()
                    print("_________________EDIT STEP 3__________________")
                    flash('Journal details updated successfully!', 'success')
                else:
                    flash('No changes to update.', 'info')
            except Exception as e:
                flash(f'Failed to update journal details due to an error: {str(e)}', 'error')
                return render_template('error_template.html'), 500
            documents = articles_read_table(user)
            return render_template('grantize/profile/journalreviewarticles.html', documents=documents)
        if "delete" in request.form:
            try:
                id_to_delete = request.form['id']
                print("-------------")
                print(id_to_delete)
                print("--------------")
                mycursor = sqlconnection.cursor()
                sql = "DELETE FROM garticles WHERE id = "+str(id_to_delete)
                mycursor.execute(sql)
                sqlconnection.commit()
                mycursor.close()
            except:
                print("REGISTER USER VARIABLES COULD NOT BE READ!!")
                return render_template('grantize/profile/journalreviewarticles.html')
            ## Code to Read
            documents = articles_read_table(user)
            return render_template('grantize/profile/journalreviewarticles.html', documents = documents)
        else:
            documents = articles_read_table(user)
            print(documents)
            return render_template('grantize/profile/journalreviewarticles.html', documents=documents)
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilejourcasestudy')
def grantizeprofilejourcasestudy():
    if session.get("loginnname"):
        return render_template('grantize/profile/resstatement.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilejourmethodologies')
def grantizeprofilejourmethodologies():
    if session.get("loginnname"):
        return render_template('grantize/profile/journalmethodologies.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilejoureditorials')
def grantizeprofilejoureditorials():
    if session.get("loginnname"):
        return render_template('grantize/profile/journaleditorials.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilejourotherarts')
def grantizeprofilejourotherarts():
    if session.get("loginnname"):
        return render_template('grantize/profile/journalotherarticles.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilebooks')
def grantizeprofilebooks():
    if session.get("loginnname"):
        return render_template('grantize/profile/books.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilebookchapters')
def grantizeprofilebookchapters():
    if session.get("loginnname"):
        return render_template('grantize/profile/bookchapters.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofileartsinnews')
def grantizeprofileartsinnews():
    if session.get("loginnname"):
        return render_template('grantize/profile/articlesinnews.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofileotherpubs')
def grantizeprofileotherpubs():
    if session.get("loginnname"):
        return render_template('grantize/profile/otherpublications.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofileresprotocols')
def grantizeprofileresprotocols():
    if session.get("loginnname"):
        return render_template('grantize/profile/researchprotocols.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofileiacucprotocols')
def grantizeprofileiacucprotocols():
    if session.get("loginnname"):
        return render_template('grantize/profile/iacucprotoocols.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofileclinicalprotocols')
def grantizeprofileclinicalprotocols():
    if session.get("loginnname"):
        return render_template('grantize/profile/clinicalprotocols.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofileconferences')
def grantizeprofileconferences():
    if session.get("loginnname"):
        return render_template('grantize/profile/conferences.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilesymposia')
def grantizeprofilesymposia():
    if session.get("loginnname"):
        return render_template('grantize/profile/symposia.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofileworkshops')
def grantizeprofileworkshops():
    if session.get("loginnname"):
        return render_template('grantize/profile/workshops.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofileseminars')
def grantizeprofileseminars():
    if session.get("loginnname"):
        return render_template('grantize/profile/seminars.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofileprofmembers')
def grantizeprofileprofmembers():
    if session.get("loginnname"):
        return render_template('grantize/profile/professionalmemberships.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofileteachingex')
def grantizeprofileteachingex():
    if session.get("loginnname"):
        return render_template('grantize/profile/teachingexperiences.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilesupermentor')
def grantizeprofilesupermentor():
    if session.get("loginnname"):
        return render_template('grantize/profile/supervisionmentoring.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilejourreviewses')
def grantizeprofilejourreviewses():
    if session.get("loginnname"):
        return render_template('grantize/profile/journalreviewAES.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilegrantreviewservices')
def grantizeprofilegrantreviewservices():
    if session.get("loginnname"):
        return render_template('grantize/profile/grantsreviewS.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilecommactivities')
def grantizeprofilecommactivities():
    if session.get("loginnname"):
        return render_template('grantize/profile/committeeactivity.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilehobbies')
def grantizeprofilehobbies():
    if session.get("loginnname"):
        return render_template('grantize/profile/hobbies.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilelangprof')
def grantizeprofilelangprof():
    if session.get("loginnname"):
        return render_template('grantize/profile/langprof.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofileotheractivities')
def grantizeprofileotheractivities():
    if session.get("loginnname"):
        return render_template('grantize/profile/otheractivities.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeprofilereferences')
def grantizeprofilereferences():
    if session.get("loginnname"):
        return render_template('grantize/profile/references.html')
    else:
        return render_template('grantize/grantize.html')
    

    
    















@app.route('/grantizerefreq')
def grantizerefreq():
    return redirect(url_for('grantize'))

@app.route('/grantizebrowsegrants', methods =["GET", "POST"])
def grantizebrowsegrants():
    global sqlconnection
    if session.get("loginnname"):
        try:
            mycursor = sqlconnection.cursor()
            sql = "SELECT id,title,grants_type,subjects FROM ggrants"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            print(result[:1])
            return render_template('grantize/dashboard/browsegrants.html', grants=result)
        except:
            print("Database Connection Not Working!!")
            return render_template('grantize/dashboard/dashboard.html')
    else:
        return render_template('grantize/grantize.html')
    
@app.route('/grantizeviewgrants', methods =["GET", "POST"])
def grantizeviewgrants():
    global sqlconnection
    if session.get("loginnname"):
        grantid = request.form['grantid']
        print("--------")
        print(grantid)
        mycursor = sqlconnection.cursor()
        sql = "SELECT id,title,subjects,description,submission_info,amount_info,cost_sharing,data_management,contacts,countries,citizenships,grants_type,applicant_types,activity_code,grant_status,open_date,intent_due_date,application_due_date,earliest_start_date,expiration_date,currency,amount_per_grant_min,amount_per_grant_max,award_min,award_max,cfda,grant_source_url FROM ggrants WHERE id = %s"
        values = (grantid,)
        mycursor.execute(sql, values)
        result = mycursor.fetchall()
        print(result[0])
        id,title,subjects,description,submission_info,amount_info,cost_sharing,data_management,contacts,countries,citizenships,grants_type,applicant_types,activity_code,grant_status,open_date,intent_due_date,application_due_date,earliest_start_date,expiration_date,currency,amount_per_grant_min,amount_per_grant_max,award_min,award_max,cfda,grant_source_url = result[0]
        return render_template('grantize/dashboard/viewgrants.html', id=id, title=title, subjects=subjects, description=description, submission_info=submission_info, amount_info=amount_info, cost_sharing=cost_sharing, data_management=data_management, contacts=contacts, countries=countries, citizenships=citizenships, grants_type=grants_type, applicant_types=applicant_types, activity_code=activity_code, grant_status=grant_status, open_date=open_date, intent_due_date=intent_due_date, application_due_date=application_due_date, earliest_start_date=earliest_start_date, expiration_date=expiration_date, currency=currency, amount_per_grant_min=amount_per_grant_min, amount_per_grant_max=amount_per_grant_max, award_min=award_min, award_max=award_max, cfda=cfda, grant_source_url=grant_source_url)
    else:
        return render_template('grantize/grantize.html')

@app.route('/grantizesearchquery', methods =["GET", "POST"])
def grantizesearchquery():
    global sqlconnection
    if session.get("loginnname"):
        user = session.get('loginid')
        if "_tokensearchquery" in request.form:
            try:
                title_query = request.form['tquery']
                mycursor = sqlconnection.cursor()
                sql = "SELECT id,title,grants_type,subjects FROM ggrants WHERE title LIKE '%"+title_query+"%'"
                mycursor.execute(sql)
                result = mycursor.fetchall()
                print(result[:1])
                return render_template('grantize/dashboard/searchquery.html', grants=result)
            except:
                print("Database Connection Not Working!!")
                return render_template('grantize/dashboard/searchquery.html')
        else:
            return render_template('grantize/dashboard/searchquery.html')
    else:
        return render_template('grantize/grantize.html')

@app.route('/grantizefavquery', methods =["GET", "POST"])
def grantizefavquery():
    global sqlconnection
    if session.get("loginnname"):
        user = session.get('loginid')
        if "_tokensearchquery" in request.form:
            try:
                title_query = request.form['tquery']
                print("_-------------")
                print(title_query)
                print("_-------------")
                mycursor = sqlconnection.cursor()
                sql = "SELECT g.id,g.title,g.grants_type,g.subjects FROM ggrants g JOIN gfavs s ON g.id = s.grantid WHERE s.userid = "+str(user)+" AND g.title LIKE '%"+title_query+"%'"
                print("_-------------")
                print(sql)
                print("_-------------")
                mycursor.execute(sql)
                result = mycursor.fetchall()
                print(result[:1])
                return render_template('grantize/dashboard/favquery.html', grants=result)
            except:
                print("Database Connection Not Working -- 1!!")
                return render_template('grantize/dashboard/favquery.html')
        else:
            try:
                mycursor = sqlconnection.cursor()
                sql = "SELECT grantid FROM gfavs WHERE userid = %s"
                values = (user,)
                mycursor.execute(sql, values)
                reqids = mycursor.fetchall()
                format_strings = ",".join([str(r[0]) for r in reqids])
                mycursor.execute("SELECT id,title,grants_type,subjects FROM ggrants WHERE id IN (%s)" % format_strings)
                result = mycursor.fetchall()
                print(result[:1])
                return render_template('grantize/dashboard/favquery.html', grants=result)
            except:
                print("Database Connection Not Working -- 2!!")
                return render_template('grantize/dashboard/favquery.html')
    else:
        return render_template('grantize/grantize.html')

@app.route('/grantizesavedquery', methods =["GET", "POST"])
def grantizesavedquery():
    global sqlconnection
    if session.get("loginnname"):
        user = session.get('loginid')
        if "_tokensearchquery" in request.form:
            try:
                title_query = request.form['tquery']
                mycursor = sqlconnection.cursor()
                sql = "SELECT g.id,g.title,g.grants_type,g.subjects FROM ggrants g JOIN gsaved s ON g.id = s.grantid WHERE s.userid = "+user+" AND g.title LIKE '%"+title_query+"%'"
                mycursor.execute(sql)
                result = mycursor.fetchall()
                print(result[:1])
                return render_template('grantize/dashboard/savedquery.html', grants=result)
            except:
                print("Database Connection Not Working - 1!!")
                return render_template('grantize/dashboard/savedquery.html')
        else:
            try:
                mycursor = sqlconnection.cursor()
                sql = "SELECT grantid FROM gsaved WHERE userid = %s"
                values = (user,)
                mycursor.execute(sql, values)
                reqids = mycursor.fetchall()
                format_strings = ",".join([str(r[0]) for r in reqids])
                mycursor.execute("SELECT id,title,grants_type,subjects FROM ggrants WHERE id IN (%s)" % format_strings)
                result = mycursor.fetchall()
                print(result[:1])
                return render_template('grantize/dashboard/savedquery.html', grants=result)
            except:
                print("Database Connection Not Working -- 2!!")
                return render_template('grantize/dashboard/savedquery.html')
    else:
        return render_template('grantize/grantize.html')
    

@app.route('/grantizesharedbyme', methods =["GET", "POST"])
def grantizesharedbyme():
    global sqlconnection
    if session.get("loginnname"):
        user = session.get('loginid')
        if "_tokensearchquery" in request.form:
            try:
                title_query = request.form['tquery']
                mycursor = sqlconnection.cursor()
                sql = "SELECT g.id,g.title,g.grants_type,g.subjects FROM ggrants g JOIN gshared s ON g.id = s.grantid WHERE s.userid = "+user+" AND g.title LIKE '%"+title_query+"%'"
                mycursor.execute(sql)
                result = mycursor.fetchall()
                print(result[:1])
                return render_template('grantize/dashboard/sharedbyme.html', grants=result)
            except:
                print("Database Connection Not Working!!")
                return render_template('grantize/dashboard/sharedbyme.html')
        else:
            try:
                mycursor = sqlconnection.cursor()
                sql = "SELECT grantid FROM gshared WHERE userid = %s"
                values = (user,)
                mycursor.execute(sql, values)
                reqids = mycursor.fetchall()
                format_strings = ",".join([str(r[0]) for r in reqids])
                mycursor.execute("SELECT id,title,grants_type,subjects FROM ggrants WHERE id IN (%s)" % format_strings)
                result = mycursor.fetchall()
                print(result[:1])
                return render_template('grantize/dashboard/sharedbyme.html', grants=result)
            except:
                print("Database Connection Not Working!!")
                return render_template('grantize/dashboard/sharedbyme.html')
    else:
        return render_template('grantize/grantize.html')

@app.route('/grantizesharedwithme', methods =["GET", "POST"])
def grantizesharedwithme():
    global sqlconnection
    if session.get("loginnname"):
        user = session.get('loginid')
        if "_tokensearchquery" in request.form:
            try:
                title_query = request.form['tquery']
                mycursor = sqlconnection.cursor()
                sql = "SELECT g.id,g.title,g.grants_type,g.subjects FROM ggrants g JOIN gsharedwith s ON g.id = s.grantid WHERE s.userid = "+user+" AND g.title LIKE '%"+title_query+"%'"
                mycursor.execute(sql)
                result = mycursor.fetchall()
                print(result[:1])
                return render_template('grantize/dashboard/sharedwithme.html', grants=result)
            except:
                print("Database Connection Not Working!!")
                return render_template('grantize/dashboard/sharedwithme.html')
        else:
            try:
                mycursor = sqlconnection.cursor()
                sql = "SELECT grantid FROM gsharedwith WHERE userid = %s"
                values = (user,)
                mycursor.execute(sql, values)
                reqids = mycursor.fetchall()
                format_strings = ",".join([str(r[0]) for r in reqids])
                print("-------")
                print(format_strings)
                print("-------")
                mycursor.execute("SELECT id,title,grants_type,subjects FROM ggrants WHERE id IN (%s)" % format_strings)
                result = mycursor.fetchall()
                print(result[:1])
                return render_template('grantize/dashboard/sharedwithme.html', grants=result)
            except:
                print("Database Connection Not Working!!")
                return render_template('grantize/dashboard/sharedwithme.html')
    else:
        return render_template('grantize/grantize.html')



































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











def connect_with_database():
    global sqlconnection
    sqlconnection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="grant"
        )
    if sqlconnection.is_connected():
        print("Database Connection Succeeded!!")
    else:
        print("Database Connection Failed!!")
        exit

 
# main driver function
if __name__ == '__main__':
    connect_with_database()
    app.run(port = 6991, debug = True)