from pywebio.input import *
from pywebio.output import *
from functools import partial

def onBtnPress(btnName, task_list, actual_task):
    task_list.remove(actual_task)
    clear('test')
    put_table([
        [i, put_buttons(['check'],onclick= partial(onBtnPress,task_list = task_list,actual_task = i))]for i in task_list 
    ],
        header= ['Task Names', 'Have you checked your tasks'],scope = 'test')


def onGoing(btnName):
    pass

def main():
    tasks = []
    with use_scope('test'):
        while True:
            task = input(label= "Enter your tasks: ",required=True)
            tasks.append(task)
            clear('test')
            put_table([
                [i, put_buttons(['check'],onclick= partial(onBtnPress,task_list = tasks,actual_task = i))]for i in tasks 
            ],
             header= ['Task Names', 'Have you checked your tasks'])
        
# main()

put_info('I am content', closable=True)

# Calling by reference and calling by value..
# hello