from flask import Flask,render_template,request
from jobs_scraper import find_jobs
from flipkart_scraper import find_deals


app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/jobs',methods=['POST'])
def scrape_jobs():
    fam_skill=request.form['familier_skill']

    jobs_data=find_jobs(fam_skill)
    return render_template('jobs.html', data=jobs_data)

### deals--------------------

@app.route('/deals')
def deals():
    return render_template('flipkart.html')

@app.route('/deals',methods=['POST'])
def scrape_deals():
    form_data=request.form['deal']
    if int(form_data)==1:
        deals_data=find_deals()
        return render_template('flipkart.html', data=deals_data)
  


if __name__=='__main__':
    app.run()