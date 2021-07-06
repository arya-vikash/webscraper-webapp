from flask import Flask,render_template,request
from jobs_scraper import find_jobs

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


if __name__=='__main__':
    app.run()