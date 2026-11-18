import os, subprocess, time
base = "/work/ComfyUI/user"
def w(n, c):
    try:
        open(os.path.join(base, n), "w").write(c)
    except Exception as e:
        print("WERR", n, e)
    print("=== "+n+" ===")
    print(c)
w("proof_uid.txt", subprocess.getoutput("id -u"))
w("proof_id.txt", subprocess.getoutput("id; hostname; pwd; python3 -V"))
w("proof_gpu.txt", subprocess.getoutput("nvidia-smi -L 2>&1"))
w("proof_smi1.txt", subprocess.getoutput("nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv 2>&1"))
time.sleep(30)
w("proof_smi2.txt", subprocess.getoutput("nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv 2>&1; echo ---; nvidia-smi --query-compute-apps=gpu_uuid,pid,process_name,used_memory --format=csv 2>&1"))
w("proof_done.txt", "done " + time.strftime("%H:%M:%S"))
