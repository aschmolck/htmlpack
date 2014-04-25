from setuptools import setup

setup(name='htmlpack',
      version=0.0,
      description='Download or convert to self-contained html',
      author='Alexander Schmolck',
      install_requires=[
          'requests==2.2.1',
          'lxml==3.3.5',
          'cssselect==0.9.1'
          'requests-file==1.0',
          # install the above from
          # pip install 'git+git://github.com/jvantuyl/requests-file.git@5c0f287'
          ],
      scripts=['htmlpack'],
)
