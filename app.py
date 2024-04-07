from flask import Flask, redirect, url_for, request, render_template
 
app = Flask(__name__)

@app.route('/grantize')
def grantize():
    return render_template('grantize/grantize.html')

@app.route('/logingrantizeoptions')
def logingrantizeoptions():
    return render_template('grantize/logingrantizeoptions.html')

@app.route('/logingrantizeres')
def logingrantizeres():
    return render_template('grantize/logingrantizeres.html')

@app.route('/logingrantizespo')
def logingrantizespo():
    return render_template('grantize/logingrantizespo.html')

@app.route('/createusergrares')
def createusergrares():
    return render_template('grantize/createusergrares.html')



@app.route('/recruitphd')
def recruitphd():
    return render_template('recruitphd.html')

@app.route('/sisterlab')
def sisterlab():
    return render_template('sisterlab.html')


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
   

 
# main driver function
if __name__ == '__main__':
    app.run(port = 6991, debug = True)