## Работа `IO_bound.py` в одном потоке
<img align="center" src="img/IO_bound_mono.png" alt="screenshot"/>
Работало целых полчаса
## В нескольких потоках:
### 5:
<img align="center" src="img/IO_bound_5.png" alt="screenshot"/>
<img align="center" src="img/IO_bound_5_sys.png" alt="screenshot"/>
### 10:
<img align="center" src="img/IO_bound_10.png" alt="screenshot"/>
### 100:
<img align="center" src="img/IO_bound_100.png" alt="screenshot"/>
<img align="center" src="img/IO_bound_100_sys.png" alt="screenshot"/>

Чем больше у нас воркеров, тем быстрее выполняется задача, и тем больше используется ресурсов: процессор, память, сеть...

## Работа `CPU_bound.py` в одном потоке
Я переписал программу так, чтобы она завершалась на 4-х сгенерированных монетах
<img align="center" src="img/CPU_bound_mono.png" alt="screenshot"/>

## Несколько потоков
### 2:
<img align="center" src="img/CPU_bound_2.png" alt="screenshot"/>
<img align="center" src="img/CPU_bound_2_sys.png" alt="screenshot"/>
### 4:
<img align="center" src="img/CPU_bound_4_time.png" alt="screenshot"/>
<img align="center" src="img/CPU_bound_4.png" alt="screenshot"/>
Дальше определённо бесполезно ставить больше, чем мои 4 ядра, мой процессор загружен на 100%
### 10:
<img align="center" src="img/CPU_bound_10.png" alt="screenshot"/>
<img align="center" src="img/CPU_bound_10_sys.png" alt="screenshot"/>

С увеличением количества задействованных ядер растёт загрузка процессора и памяти, а время работы в среднем уменьшается.
Сеть, как ни странно, тут вообще не используется, так что она никак не загружена в любом случае.
Как можно заметить, наращивать количество воркеров больше количества ядер (у меня 4) бесполезно.