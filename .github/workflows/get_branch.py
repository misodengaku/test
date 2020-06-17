import os
import re

github_ref = os.getenv('GITHUB_REF')
github_sha = os.getenv('GITHUB_SHA')

if 'refs/tags/' in github_ref:
    print('::set-output name=RELEASE_NAME::tag-%s' % re.sub('^refs/tags/', '', github_ref))
elif 'refs/heads/' in github_ref:
    print('::set-output name=RELEASE_NAME::branch-%s-%s' % (re.sub('^refs/heads/', '', github_ref), github_sha))
else:
    print('::set-output name=RELEASE_NAME::refs-%s' % re.sub('^refs/', '', github_ref))