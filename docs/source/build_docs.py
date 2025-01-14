import os
import yaml
import subprocess


# a single build step, which keeps conf.py and versions.yaml at the main branch
# in general we use environment variables to pass values to conf.py, see below
# and runs the build as we did locally
def build_doc(version, language, tag):
    print(f"Will try to build for {(version, language, tag)}")
    os.environ["current_version"] = version
    os.environ["SOURCEDIR"] = "source"
    os.environ["BUILDDIR"] = "build"
    os.environ["current_language"] = language
    subprocess.run("git checkout " + tag, shell=True)
    subprocess.run("git checkout develop -- ./source/conf.py", shell=True)
    subprocess.run("git checkout develop -- ./source/versions.yaml", shell=True)
    subprocess.run("make html", shell=True)


# a move dir method because we run multiple builds and bring the html folders to a
# location which we then push to github pages
def move_dir(src, dst):
    print(f"Moving from {src} to {dst}")
    subprocess.run(["mkdir", "-p", dst])
    subprocess.run("mv " + src + "* " + dst, shell=True)


if __name__ == "__main__":
    # to separate a single local build from all builds we have a flag, see conf.py
    os.environ["build_all_docs"] = str(True)
    os.environ["pages_root"] = "https://spjuhel.github.io/BoARIO"
    # manually the main branch build in the current supported languages
    build_doc("latest", "en", "origin/main")
    move_dir("./build/html/", "./pages/")
    # build_doc("latest", "de", "main")
    # move_dir("./_build/html/", "../pages/de/")

    # reading the yaml file
    with open("./source/versions.yaml", "r") as yaml_file:
        docs = yaml.safe_load(yaml_file)

        # and looping over all values to call our build with version, language and its tag
    for version, details in docs.items():
        tag = details.get("tag", version)
        for language in details.get("languages", []):
            build_doc(version, language, tag)
            move_dir("./build/html/", "./pages/" + version + "/" + language + "/")
