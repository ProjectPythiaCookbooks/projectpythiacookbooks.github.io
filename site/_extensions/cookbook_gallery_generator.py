import yaml
from itertools import chain
from gallery_generator import build_from_repos, generate_menu, generate_repo_dicts


def main(app):

    with open('cookbook_gallery.txt') as fid:
        all_items = fid.readlines()

    repo_dicts = generate_repo_dicts(all_items)

    title = 'Cookbooks Gallery'

    stext1 = "Pythia Cookbooks provide example workflows on more advanced and domain-specific problems developed by the Pythia community. Cookbooks build on top of skills you learn in Pythia Foundations."
    stext2 = "Cookbooks are created from Jupyter Notebooks that we strive to binderize so each Cookbook can be executed in the cloud with a single click from your browswer. See documentation [here](https://foundations.projectpythia.org/preamble/how-to-use.html#interacting-with-jupyter-notebooks-in-the-cloud-via-binder) for details. In some instances executing a Cookbook will require downloading the Notebook to your local laptop or desktop as described [here](https://foundations.projectpythia.org/preamble/how-to-use.html#interacting-with-jupyter-books-locally)."
    stext3 = "Interested in contributing a new Cookbook or contributing to an existing Cookbook? Great! Please see the [Project Pythia Contributor's Guide](https://projectpythia.org/contributing.html) and Cookbook-specific information [here](https://github.com/ProjectPythiaCookbooks/.github/blob/main/CONTRIBUTING.md)."
    subtext = stext1 + '<br><br>' + stext2 + '<br><br>' + stext3

    subtext = ''
    with open('cookbook_gallery_subtext.txt') as fid:
        for line in fid:
            subtext = subtext + line

    submit_btn_link = 'https://github.com/ProjectPythiaCookbooks/projectpythiacookbooks.github.io/issues/new?assignees=ProjectPythiaCookbooks%2Feducation&labels=content%2Ccookbook-gallery-submission&template=update-cookbook-gallery.yaml&title=Update+Gallery+with+new+Cookbook'
    submit_btn_txt = 'Submit a new Cookbook'
    menu_html = generate_menu(repo_dicts, submit_btn_txt=submit_btn_txt, submit_btn_link=submit_btn_link)
    
    build_from_repos(repo_dicts, 'index', title=title, subtext=subtext, menu_html=menu_html)


def setup(app):
    app.connect('builder-inited', main)
