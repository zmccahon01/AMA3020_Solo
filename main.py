
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


np.random.seed(5)

dt = 0.001
sd = np.sqrt(dt)

a = 0.1
b = 0.2
T = 1000
S = 1

xlocs = np.linspace(0, T, 6)
xlabs = np.char.mod('%.1f', xlocs*dt)


  
grads = []
for i in range(3):
  
  S = 1
  S_t = [S]  
  W = 0
  W_t = np.array([0])
  for j in range(T):
    dW = np.random.normal(scale=sd)
    W += dW
    W_t = np.append(W_t, W)
       
    dS = a * S * dt + b * S * dW
    S += dS
    S_t.append(S)
      
  
  plt.plot(np.arange(1, T + 2), S_t, label=('$S_' + str(i) + '$'))
  
  log_S_t = np.log(S_t)
  drift = log_S_t - b*W_t 
  grad = (drift[-1] - drift[0])/ (T*dt)
  grads.append(grad)
  
  #plt.plot(np.arange(1, T + 2), log_S_t, label=('$log(S_' + str(i) + ')$'))
  #plt.plot(np.arange(1, T + 2), drift, '--', label=('$drift_' + str(i) + '$'))


print(np.mean(grads))

plt.plot(np.arange(1, T + 2), S_t)
plt.legend()
plt.xlabel('t')
plt.ylabel('S(t)')
plt.xticks(xlocs, xlabs)
plt.savefig('S_t.png', dpi=600)
plt.close()
'''
plt.plot(np.arange(1, T + 2), W_t)
plt.xlabel('t')
plt.ylabel('W(t)')
plt.xticks(xlocs, xlabs)
plt.savefig('W_t.png', dpi=600)
plt.close()
'''

plt.plot(np.arange(1, T + 2), log_S_t, label='log(S)')
plt.plot(np.arange(1, T + 2), drift, label='drift')
plt.xlabel('t')
plt.xticks(xlocs, xlabs)
plt.legend()
plt.savefig('log_S_t.png', dpi=600)
plt.close()

T = 1000
dt = 0.001
xlocs = np.linspace(0, T, 6)
xlabs = np.char.mod('%.1f', xlocs*dt)
S_ts = np.zeros([T+1, 25000])
for i in range(25000):
  
  S = 1
  S_t = [S]
  
  for j in range(T):
    dW = np.random.normal(scale=sd)

    dS = a * S * dt + b * S * dW
    S += dS
    S_t.append(S)

  if(i % 10 == 0):
    plt.plot(S_t)
  S_ts[:, i] = S_t
S_final = S_ts[-1, :]
S_t_avg = np.mean(S_ts, axis=1)
print(S_t_avg[-1])
plt.xlabel('t')
plt.ylabel('S(t)')
plt.xticks(xlocs, xlabs)
plt.savefig('temp.png')

plt.close()
plt.plot(S_t_avg)
plt.xlabel('t')
plt.ylabel('Average S(t)')
plt.xticks(xlocs, xlabs)
plt.savefig('avg_S_t.png', dpi=600)
plt.close()


plt.hist(S_final, bins=50)
mn = np.mean(S_final)
plt.axvline(mn, color = 'r', linestyle = 'dashed', linewidth = 1)
plt.savefig('hist.png')
plt.close()

vals = np.linspace(0, 1, 11)
means = []
stds = []
b=0.1
for a in vals:
    S_final = []
    for j in range(10000):
      
      S = 1
      S_t = [S]
      
      for l in range(T):
        dW = np.random.normal(scale=sd)
        
        dS = a * S * dt + b * S * dW
        S += dS
        S_t.append(S)
        
      S_final.append(S)
    stds.append(np.std(S_final))
    means.append(np.mean(S_final))
plt.plot(vals, means, label='mean')
plt.errorbar(vals, means, yerr=stds, fmt='o', label='error')
plt.xlabel('a')
plt.ylabel('Mean / standard deviation')
plt.legend()
plt.savefig('mean_std_a.png')
plt.close()

means = []
stds = []
a=0.1
for b in vals:
    S_final = []
    for j in range(10000):
      
      S = 1
      S_t = [S]
      
      for l in range(T):
        dW = np.random.normal(scale=sd)
        
        dS = a * S * dt + b * S * dW
        S += dS
        S_t.append(S)
        
      S_final.append(S)
    stds.append(np.std(S_final))
    means.append(np.mean(S_final))
plt.plot(vals, means, label='mean')
plt.errorbar(vals, means, yerr=stds, fmt='o', label='error')
plt.xlabel('b') 
plt.ylabel('Mean / standard deviation')
plt.legend()
plt.savefig('mean_std_b.png')
plt.close()

