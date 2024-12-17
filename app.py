from flask import Flask, request
import function.cpu_stress_module as cpu_stress_
import function.gpu_stress_module as  gpu_stress_
import function.memory_stress_module as memory_stress_
import function.disk_stress_module as disk_stress_
import function.network_stress_module as network_stress_
import function.all_in_one_stress_module as all_in_one_
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

# @app.route('/cpuStress', methods = ['GET', 'POST'])
# def cpu_stress_test_func():
#     # print(type(duration))
#     return cpu_stress_.cpu_stress_func()

#Ex.) http://10.0.2.193:5000/cpuStress?duration=5&cpu_num=2
@app.route('/cpu_stress')
def cpu_stress_function():
    parameter_dict = request.args.to_dict(flat=False)
    # core 단위 burst
    # cpu_stress_.cpu_stress_func2(int(parameter_dict['cpu_num'][0]), int(parameter_dict['duration'][0])) 
    # percentage burst
    cpu_stress_.cpu_stress_ng_func(parameter_dict.get('cpu_num')[0], int(parameter_dict['duration'][0]), parameter_dict.get('percentage')[0])
    return 'cpu stress func'

@app.route('/gpu_stress')
def gpu_stress_test_func():
    parameter_dict = request.args.to_dict(flat=False)
    gpu_stress_.gpu_stress_all(int(parameter_dict['duration'][0]))
    return 'gpu stress func'

#Ex.) http://10.0.2.193:5000/memoryStress?duration=5&mem_amount=600
@app.route('/memory_stress')
def memory_stress_test_func():
    parameter_dict = request.args.to_dict(flat=False)
    memory_stress_.memory_stress_func(int(parameter_dict['duration'][0]), int(parameter_dict['mem_amount'][0]))
    return 'memory stress func'

#Ex.) http://10.0.2.193:5000/diskStress?duration=5&size_mb=100
@app.route('/disk_stress')
def disk_stress_test_func():
    parameter_dict = request.args.to_dict(flat=False)
    # disk_stress_.disk_stress_func(int(parameter_dict['duration'][0]), int(parameter_dict['size_mb'][0]))
    disk_stress_.multi_processing_disk_stress_func(int(parameter_dict['duration'][0]), int(parameter_dict['size_mb'][0]))
    
    return 'disk stress func'

#Ex.) http://10.0.2.193:5000/networkStress?duration=5&mode=preprocess&net_url=localhost&net_port=5000&network_mode=prep
@app.route('/network_stress')
def network_stress_test_func():
    parameter_dict = request.args.to_dict(flat=False)
    network_stress_.network_stress_func(int(parameter_dict['duration'][0]), parameter_dict['net_url'][0], parameter_dict['net_port'][0], parameter_dict['network_mode'][0])
    return 'network stress func'

#Ex.) http://10.0.2.193:5000/stress_test?duration=5&mode=preprocess&net_url=localhost&net_port=5000&network_mode=prep&cpu_num=2&mem_amount=600&size_mb=100
# @app.route('/stress_test')
# def all_in_one_stress_test_function():
#     parameter_dict = request.args.to_dict(flat=False)
#     all_in_one_.all_in_one_test_func(
#         int(parameter_dict['duration'][0]),
#         parameter_dict['mode'][0], 
#         parameter_dict['net_url'][0], 
#         parameter_dict['net_port'][0], 
#         parameter_dict['network_mode'][0],
#         int(parameter_dict['cpu_num'][0]),
#         int(parameter_dict['mem_amount'][0]),
#         int(parameter_dict['size_mb'][0])
#     )

#     return 'all_in_one_stress_test_function'

#Ex.) http://10.0.2.193:5000/stress_test?cpu_stress=True&gpu_stress=False&memory_stress=False&disk_stress=True&network_stress=True&duration=5&mode=preprocess&net_url=localhost&net_port=5000&network_mode=prep&cpu_num=2&mem_amount=600&size_mb=100
'''
dictionary examples
{
    'cpu_stress': ['True'], 
    'gpu_stress': ['False'], 
    'memory_stress': ['False'], 
    'disk_stress': ['True'], 
    'network_stress': ['True'], 
    'duration': ['5'], 
    'mode': ['preprocess'], 
    'net_url': ['localhost'],
    'net_port': ['5000'],
    'network_mode': ['prep'],
    'cpu_num': ['2'],
    'mem_amount': ['600'],
    'size_mb': ['100']
}
'''
@app.route('/aio')
def all_in_one_stress_test_function():
    parameter_dict = request.args.to_dict(flat=False)
    print(parameter_dict)
    print('type of: ', type(parameter_dict.get('duration')))
    all_in_one_.all_in_one_test_func(
        parameter_dict
    )
    
    return 'all_in_one_stress_test_function'

@app.route('/testuri')
def testfunction():
    parameter_dict = request.args.to_dict(flat=False)
    # print('parameter_dict: ', parameter_dict)
    cpu_stress_.cpu_stress_ng_func(parameter_dict.get('cpu_num')[0], int(parameter_dict['duration'][0]), parameter_dict.get('persentage')[0])

    return 'testfunction'
if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)