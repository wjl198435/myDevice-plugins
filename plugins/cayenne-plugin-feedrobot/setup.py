import os
import subprocess

from setuptools import setup

# output = subprocess.check_output("dpkg-query -W --showformat='${Status}' sense-hat".split(' '))
# package_installed = 'install ok installed' in output.decode()
reboot_required = False
# if not package_installed:
#     print('Updating package list')
#     subprocess.call(['apt-get', 'update'])
#     print('Installing sense-hat package')
#     reboot_required = subprocess.call(['apt-get', 'install', '-y', 'sense-hat']) == 0
#
classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Home Automation',
               'Topic :: System :: Hardware',
               'Topic :: System :: Monitoring']

try:
    os.makedirs('/etc/myDevices/plugins/cayenne-plugin-feedrobot/data')
except FileExistsError:
    pass

setup(name             = 'feedrobot',
      version          = '0.1.15',
      author           = 'wangjinliang',
      author_email     = 'N/A',
      description      = 'myDevices Cayenne Feed Robot plugin',
      keywords         = 'myDevices IoT Cayenne Feed Robot plugin',
      url              = 'https://www.haiwar.com/',
      classifiers      = classifiers,
      packages         = ['feedrobot',
                          'feedrobot.weightsensors',
                          'feedrobot.tempsensors',
                          'feedrobot.distancesensors',
                          'feedrobot.gpiosensors'],
      data_files       = [
                        #   ('/etc/myDevices/plugins/cayenne-plugin-feedrobot/data', ['data/NA4-350kg-Tail.swp']),
                        #   ('/etc/myDevices/plugins/cayenne-plugin-feedrobot/data', ['data/NA4-350kg-Head.swp']),
                        #   ('/etc/myDevices/plugins/cayenne-plugin-feedrobot/data', ['data/5kg-food.swp']),
                            ('/lib/systemd/system', ['data/feedrobot.service'])]
      )

subprocess.call(['systemctl', 'daemon-reload'])
subprocess.call(['systemctl', 'preset', 'feedrobot.service'])
subprocess.call(['systemctl', 'start', 'feedrobot.service'])

if reboot_required:
    answer = input('\nFeed Robot requires a reboot to finish the install. Reboot now? [Y/n]: ').lower()
    if answer not in ('n', 'no'):
        os.system('reboot')
