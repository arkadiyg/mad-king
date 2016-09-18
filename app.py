from flask import Flask, request, render_template
import inventory
import persist as persister

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recon')
def recon():
    who = inventory.Who()
    instances = inventory.Instance().get_all_running()
    return render_template('recon.html', instances=instances, who=who)

@app.route('/disrupt')
def disrupt():
    trails = inventory.CloudTrail().get_trails()
    return render_template('disrupt.html', trails=trails)

@app.route('/persist')
def persist():
    persist_attack = persister.Persistence()
    return render_template('persist.html', persist=persist_attack)

# We only need this for local development.
if __name__ == '__main__':
    app.run()
