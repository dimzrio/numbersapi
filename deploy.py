from argparse import ArgumentParser
import sys
import subprocess

parser = ArgumentParser(description='Deployment CLI')
parser.add_argument (
	'-e', '--env', 
	action='store', 
	dest="ENVIRONMENT", 
	default='development', 
	help='Set deployment environment, options: [development, staging, production]',
    required=True
	)

parser.add_argument (
	'-s', '--stack', 
	action='store', 
	dest="STACK", 
	help='options: [frontend, backend]',
    required=True
	)

if len(sys.argv) == 1:
	print(parser.print_help())
	sys.exit(0)

args = parser.parse_args()
env = args.ENVIRONMENT
stack = args.STACK

if not args.STACK:
    print(parser.print_help())
    sys.exit(0)

if stack == 'frontend' or stack == 'backend':
    pass
else:
    print(parser.print_help())
    sys.exit(0)

def command_exec(cmd):
    status = True

    shellexec = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = shellexec.communicate()[0]

    if shellexec.returncode != 0:
        status = False

    return status, stdout

def start_task(stack=None, env=None):
    build = """
    echo '[+] Build process...' \
    && cd {0} \
    && sudo docker build -t registry-intl.ap-southeast-1.aliyuncs.com/dimzrio/numbersapi:{0}-{1} . \
    && sudo docker push registry-intl.ap-southeast-1.aliyuncs.com/dimzrio/numbersapi:{0}-{1}
    """.format(stack, env)

    build_task = command_exec(build)
    print(build_task[1].decode('utf-8'))

    if build_task[0]:
        if stack == 'frontend':
            backendURL = 'http://backend.{}.svc.cluster.local:8080/info'.format(env)
            deploy = "cd helm/frontend && helm upgrade --install frontend . -n {0} --wait --set env={0} --set backendURL={1}".format(env, backendURL)
        elif stack == 'backend':
            deploy = "cd helm/backend && helm upgrade --install backend . -n {0} --wait --set env={0}".format(env)
        else:
            sys.exit(1)
            
        print(deploy)
        deploy_task = command_exec(deploy)

        print(deploy_task[1].decode('utf-8'))

        if deploy_task[0]:
            print('Success deploy {0} to {1}...n_nb'.format(stack, env))
        else:
            print('Success deploy {0} to {1}...T_T'.format(stack, env))

# Staring Deploy
if stack == 'production' or stack == 'staging' or stack == 'development':
    print('Starting deployment process...')
    start_task(stack=stack, env=env)
else:
    print(parser.print_help())
    sys.exit(0)