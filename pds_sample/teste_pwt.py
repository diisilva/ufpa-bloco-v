import csv
import pywt
import matplotlib.pyplot as plt
import numpy as np

path_csv = '/home/diego-silva/Documentos/pds_sample/sample_2.txt'
list_values = []

def listValues(path):
        
    with open(path, 'r') as f:
        # values_str = [line.strip() for line in f]
        for line in f:
            print line
            # break
            list_values.append(float(line))

    # print list(values_str[0])

    # for item in values_str:
    #     list_values.append(float(item))

    # # print type(list_values[0])
    return list_values

def pywtGraphics(listDistrib,typeDWT):

    (ca, cd) = pywt.dwt(listDistrib,typeDWT)

    print 'ca\n'
    print ca

    print 'cd'
    print cd

    # cat = pywt.threshold.soft(ca, np.std(ca)/2)
    # cdt = pywt.threshold.soft(cd, np.std(cd)/2)
    cat = pywt.threshold(ca,np.std(ca)/2,'soft')
    cdt = pywt.threshold(cd,np.std(cd)/2,'soft')

    ts_rec = pywt.idwt(cat, cdt, typeDWT)

    plt.close('all')

    plt.subplot(211)
    # Original coefficients
    plt.plot(ca, '--*b')
    plt.plot(cd, '--*r')
    # Thresholded coefficients
    plt.plot(cat, '--*c')
    plt.plot(cdt, '--*m')
    plt.legend(['ca','cd','ca_thresh', 'cd_thresh'],loc=0)
    # 'ca_thresh', 'cd_thresh'], loc=0)
    plt.grid('on')

    plt.subplot(212)
    plt.plot(listDistrib)
    plt.hold('on')
    plt.plot(ts_rec, 'r')
    plt.legend(['original signal', 'reconstructed signal'])
    plt.grid('on')
    plt.show()

list_distrib = listValues(path_csv)

print 'list_distrib\n'
print list_distrib
dwt = 'db2'
pywtGraphics(list_distrib,dwt)
