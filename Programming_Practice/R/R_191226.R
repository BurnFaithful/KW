setwd("C:/Users/user/Desktop/Youngmin/KW/Programming_Practice/R/R_data") # comment
getwd()
print(1+2)
data1 = 1
data1 = '1'
data1 = 2.1

class(data1)

cat(1, 2, 3, 4)
cat('a', 'b', 'c')

4 / 2 # 실수 몫 값
5 / 2

4 %% 2 # 나머지 값
5 %% 2

5 %/% 2 # 정수 몫 값
4 %/% 2

3^2
9^2
4**2

10
100
1000
10000
100000 # 10만부터 지수형태로 출력
1e2
3e-1
1 + 2
1 + '2'
1 + as.numeric('2') # 형 변환 : as.~~

'1' + '2'
as.numeric('1') + as.numeric('2')
'data2'
data3
# &, | logical operator

# NA : 잘못된 값이 들어온 경우
# NULL : 값이 없을 경우
cat(1, NA, 2)
cat(1, NULL, 2)
sum(1, 2, NA) # NA로 연산하면 결과가 무조건 NA
sum(1, 2, NULL)
sum(1, 2, NA, na.rm = T)

# Factor형 : 여러번 중복되어 나오는 데이터
txt1 = read.csv("factor_test.txt")
txt1
txt2 = factor(txt1$blood)
txt2
summary(txt2)
sex1 = factor(txt1$sex)
summary(sex1)

# 날짜, 시간
Sys.Date()
Sys.time()
date()
class("2019-12-26")
class(as.Date("2019-12-26"))
as.Date("26-12-2019", format="%d-%m-%Y") # y는 2글자, Y는 4글자
as.Date("2019년 12월 26일", format="%Y년 %m월 %d일")
as.Date("26122019", format="%d%m%Y")
as.Date(100, origin=Sys.Date())
as.Date(Sys.Date()) - as.Date(-100, origin=Sys.Date())
# POSIXlt : 년, 월, 일
# POSIXct : 년, 월, 일, 시, 분, 초
as.Date("2019-12-26 18:20:00") - as.Date(Sys.time())
as.POSIXct("2019-12-26 18:20:00") - as.POSIXct(Sys.time())

install.packages("lubridate")
library(lubridate)

date <- now()
date
year(date)
month(date)
day(date)
wday(date, label=T)
hour(date)
minute(date)
second(date)
date <- date - days(10)
date
date <- date + days(10)
date
seq(as.Date("2020-01-01"), as.Date("2020-12-31"), "month")
seq(as.Date("2020-01-01"), as.Date("2200-12-31"), "year")

a1 = 1, 2, 3, 4, 5, 6
a1 = 1:10 # 연속적인 숫자값에 대해서만 가능
a1
a1 = 'a' : 'f' # 문자는 불가능
a1
a1 = 10; b1=20
a1 + b1
objects() # 만들어놓은 변수들 확인 가능
rm(list=ls())

# 데이터처리 객체
# 동일 데이터 타입
# 스칼라 : 단일 데이터 처리
# 벡터 : 1차원 배열(스칼라를 여러 개 합친 것)
# Matrix : 2차원 배열(벡터를 여러 개 합친 것)
# 배열(array) : 3차원 배열(매트릭스를 여러 개 쌓아놓은 것)
# 
# 다른 데이터 타입
# list : key&value 형태로 저장
# DataFrame : DB의 테이블과 유사

c(1, 2, 3, 4, 5) # 벡터
c('a', 'b', 'c', 'd', 'e')
c(1, 2, 3, 'a') # 강제로 형변환

# 1. c() 함수로 벡터 생성
# 2. 인덱스는 1로 시작
# 3. 하나의 자료형만 사용 가능
# 4. 결측값은 'NA'
# 5. NULL은 어떤 형식도 취하지 않는 특별한 객체
v1 = c(1, 2, 3, 4, 5)
v1
v1[3]
v1[-3]
v1[2:4]
v1[-2:-4]
v1[2] = 6
v1
v1 = c(v1, 7)
v1
v1[9] = 9
v1
v1 = append(v1, 10, after=3)
v1 = append(v1, c(100, 110), after=4)
v1
c(1, 2, 3) + c(2, 3, 4)
v1 = c(1, 2, 3)
v2 = c(2, 3)
v1 + v2 # 모자란 인덱스를 채워줘서 3 + 2 값을 마지막 인덱스에서 연산
v2 = c('2', '3', '4')
v1 + v2
union(v1, v2)
v1 = c(1, 2, 3)
v2 = c(3, 4, 5)
setdiff(v1, v2)
intersect(v1, v2)

# 벡터에 컬럼 이름 지정
fruits = c(10, 20, 30)
fruits
names(fruits) = c('apple', 'banana', 'peach')
fruits

v3 = seq(1, 5)
v3
v4 = seq(-1, -10)
v4
v5 = rep(1:3, 2)
v5
v5 = rep(1:3, each=3) # 값마다 각각 반복
v5
length(v1)
NROW(v1)
v6 = c(1, 3, 5, 7, 9)
3 %in% v6
4 %in% v6

# 행렬 : matrix
# 1. 벡터의 집합
# 2. 모든 row, column은 데이터 타입이 동일
# 3. 기본적으로 열로 생성
# 4. 다른 데이터타입의 데이터를 저장할 경우 데이터프레임을 사용
m1 = matrix(c(1, 2, 3, 4), nrow=2, byrow=T) #nrow : 행 갯수, byrow : 행 우선
m1
m1[,1]
m1[1,]
m1[1,1]
m2 = matrix(c(1, 2, 3,
              4, 5, 6,
              7, 8, 9), nrow=3, byrow=T)
m2
m2[,2]
m2[3,]

# 행 추가 : rbind()
# 열 추가 : cbind()
m3 = rbind(m2, c(10, 11, 12))
m3
m3 = cbind(m3, c(13, 14, 15, 16))
m3
m3 = cbind(m3, c(17, 18, 19))
m3
colnames(m3)=c('1st', '2nd', '3rd', '4th', '5th')
m3
arr1 = array(c(1:12), dim=c(2, 2, 3))
arr1
arr1[1,1,2]

# list : 서로 다른 데이터 타입
list1 = list(name='권영민',
             addr='의정부시',
             tel='010-3346-9910',
             pay=3000)
list1
list1$name
list1$pay
list1[1:3]
list1$birth = as.Date('1994-04-09')
list1
class(list1$birth)
list1$name[length(list1$name) + 1] = '이순신'
list1
list1$birth = NULL
list1
list1$name[length(list1$name) - 1] = NA
# NULL을 넣으면 'replacement has length zero' Error 발생
list1

# DataFrame
# 1. 벡터로부터 데이터프레임 생성 : 각 컬럼별로 먼저 생성한 후 data.frame으로
# 모든 컬럼을 합친다.

no = c(1, 2, 3, 4)
name = c('apple', 'banana', 'peach', 'grape')
price = c(500, 200, 100, 50)
qty = c(6, 2, 4, 7)
sales = data.frame(NO=no, NAME=name, PRICE=price, QTY=qty)
sales

# 2. 행렬로부터 데이터프레임 생성
sales2 = matrix(c(1, 'apple', 500, 5,
                3, 'banana', 100, 4,
                2, 'peach', 200, 2,
                4, 'grape', 50, 7),
                nrow=4, byrow=T)
sales2
df1 = data.frame(sales2, stringsAsFactors = F)
df1
names(df1)=c('NO', 'NAME', 'PRICE', 'QTY')
df1
class(sales)
class(sales2)
class(df1)
str(sales)
str(df1)

df1$QTY = as.numeric(df1$QTY)

sales$NAME
sales[,3]
sales[c(1,2),]
sales[,c(1:3)]

subset(sales, qty > 5)
subset(df1, QTY >= 5)


# 데이터 프레임 합치기 : rbind(), cbind(), merge()
no = c(1, 2, 3)
name = c('apple', 'banana', 'peach')
price = c(100, 200, 300)
df1 = data.frame(NO=no, NAME=name, PRICE=price)
df1
no = c(10, 20, 30)
name = c('train', 'car', 'ship')
price = c(1000, 2000, 3000)
df2 = data.frame(NO=no, NAME=name, PRICE=price)
df2
df3 = cbind(df1, df2)
df3
df4 = rbind(df1, df2)
df4


df1 = data.frame(name=c('apple', 'banana', 'peach'), price=c(300, 200, 100))
df2 = data.frame(name=c('apple', 'cherry', 'berry'), qty=c(10, 20, 30))
df1; df2

merge(df1, df2, all=T)
df1
new = data.frame(name='mango', price=400)
df2 = rbind(df1, new)
df1; df2
df3 = rbind(df2, data.frame(name='berry', price=500))
df3
df4 = cbind(df3, data.frame(qty=c(10, 20, 30, 40, 50)))
df4

# 데이터프레임 특정 컬럼만 추출하여 새로운 형태 만들기
no = c(1, 2, 3, 4, 5)
name = c('홍길동', '이순신', '유관순', '김유신', '윤동주')
addr = c('서울시', '의정부시', '부산시', '광주시', '제주시')
tel = c(1111, 2222, 3333, 4444, 5555)
hobby = c('놀기', '먹기', '자기', '놀먹', '자먹')
member = data.frame(NO=no, NAME=name, ADDR=addr, TEL=tel, HOBBY=hobby)
member
mem1 = subset(member, select = c(NO, NAME, ADDR))
mem1
mem2 = subset(member, select = -TEL)
mem2
colnames(mem2)=c('번호', '이름', '주소', '취미')

# nrow, ncol, names, rownames()==row.names(), colnames()==col.names()
# 데이터 수정하기
install.packages('dplyr')
library(dplyr)

df1 = data.frame(var1=c(1, 2, 3), var2=c(2, 3, 2))
df1
df2 = df1
df2 = rename(df1, v2=var2)
df2
# 파생 변수
df3 = data.frame(var1=c(4, 3, 8), var2=c(2, 6, 1))
df3
df3$sum = df3$var1 + df3$var2
df3
df3$mean = df3$sum / 2
df3

install.packages('ggplot2')
library(ggplot2)
mpg
mpg1 = mpg
mpg1 = rename(mpg1, city=cty)
mpg1 = rename(mpg1, highway=hwy)
mpg1
head(mpg1, 7)
tail(mpg1, 20)

list.files(recursive = T, all.files = T)
sc1 = scan("scan_1.txt") # 배열의 형태로 저장
sc1
sc2 = scan("scan_2.txt", what = "")
sc2
sc3 = scan("scan_3.txt", what = "")
sc3
sc4 = scan("scan_4.txt", what = "")
sc4
sc5 = scan(what = "")
sc5

# readline() : 한 줄 읽어들이기
in1 = readline()
in1
in2 = readline("R U ok?")
in2

# readLines() : 파일을 배열에 저장
in3 = readLines("scan_4.txt")
in3
fruits = read.table("fruits.txt", header = T) # 데이터를 불러들여 데이터프레임에 저장. header가 파일에 존재하면 header = T
fruits
fruits = read.table("fruits_2.txt", header = F, skip = 2, nrow=2) # skip의 경우 공백라인, 주석문 라인을 포함함
fruits
fruits4 = read.csv("fruits_4.csv", header = F)
fruits4

label = c('NO', 'NAME', 'PRICE', 'QTY')
fruits4 = read.csv('fruits_4.csv', header = F, col.names = label)
fruits4

install.packages("googleVis")
library(googleVis)

install.packages("sqldf")
library(sqldf)
Fruits
write.csv(Fruits, "Fruits_sql.csv", quote = F, row.names = F)
f2 = read.csv.sql("Fruits_sql.csv", sql="select * from file where Year=2008")
f2

txt1 = readLines("write_test.txt")
txt1
write(txt1, "write_test2.txt")

txt2 = read.table("table_test.txt", header = T)
txt2
write.table(txt2, "table_test2.txt")


# 191227
# aggregate() : 다양한 함수를 사용하여 계산결과를 출력
# apply()
# cor() : 상관 함수
# cumsum() : 누적합
# cumprom() : 누적곱
# diff() : 차이나는 부분을 찾아냄
# length()
# max()
# min()
# mean() : 평균
# median() : 중간값
# order()
# prod()
# range() : 범위값
# rank()
# rev() : 역순
# sd() : 표준편차
# sort()
# sum() : 총합
# summary()
# sweep() : 일괄차
# tapply() : 벡터에서 주어진 함수 연산
# var() : 분산
v1 = c(1, 2, 3, 4, 5)
v2 = c('a', 'b', 'c', 'd', 'e')
max(v2)
mean(v1)
mean(v2)
sd(v1)
sd(v2)
sum(v1)
var(v1)

# aggregate() : 데이터프레임 상대로 주어진 함수값을 구함
# aggregate(계산될 컬럼 ~ 기준될 컬럼, 데이터, 함수)
library(googleVis)
Fruits
aggregate(Sales~Year, Fruits, sum)
aggregate(Sales~Fruit, Fruits, sum)
aggregate(Sales~Fruit+Year, Fruits, max)

#apply() : matrix()에서 유용하게 사용(행, 열을 대상으로 작업)
#apply(대상, 행/열, 적용함수)
m1 = matrix(c(1, 2, 3,
              4, 5, 6),nrow = 2, byrow = T)
m1
apply(m1, 1, sum)
apply(m1, 2, max)
apply(m1[,c(2, 3)], 2, sum)

#lapply(), sapply() : list 처리
#lapply/sapply(대상, 적용함수)
l1 = list(Fruits$Sales)
l1
l2 = list(Fruits$Profit)
l2
lapply(c(l1, l2), max)
sapply(c(l1, l2), max)
lapply(Fruits[,c(4, 6)], max)
sapply(Fruits[,c(4, 6)], max)

#tapply(), mapply() : 데이터셋의 특정 요소(factor)를 처리
#tapply(출력값, 기준컬럼, 적용함수)
Fruits
tapply(Sales, Fruit, sum)
#attach() : 변수를 직접 사용하기 위한 함수
attach(Fruits)
tapply(Sales, Fruit, sum)
tapply(Sales, Year, sum)

#mapply(함수, 벡터1, 벡터2, ...) : 벡터나 리스트를 데이터프레임처럼 처리
#mapply() : 만약 데이터프레임이 아닌 벡터나 리스트형태로 데이터들이 있을 때 마치 데이터프레임처럼 연산을 해주는 함수. 단, 벡터들의 요소 갯수가 동일해야 한다.
v1 = c(1, 2, 3, 4, 5)
v2 = c(10, 20, 30, 40, 50)
v3 = c(100, 200, 300, 400, 500)
mapply(sum, v1, v2, v3)

#sweep() : 한꺼번에 차이 구하기 -> 여러 데이터들에게 일괄적으로 기준을 적용
#벡터, 매트릭스, 배열, 데이터프레임으로 구성된 여러 데이터들에 동일한 기준을 적용시켜 차이나는 부분을 일목요연하게 보여주는 함수
m1
a = c(1, 1, 1)
sweep(m1, 2, a) # 2가 행, 1이 열

#ceiling(), floor() : 버림
v1 = c(1.2, 1.9, 2.1)
ceiling(v1) # 올림
choose(5, 3) # 조합
floor(3.2) # 내림
floor(v1)
trunc(v1)

# 사용자 정의 함수
# 함수명 = function(인수 또는 입력값) {
# 계산식 ..
# }
# 
f1 = function(a) {
  b = a^2
  return(b)
}

f1(3)

f1 = function(a, b) {
  b = a^2
  return(b)
}

f1(3, 2)

s1 = Fruits$Sales
s1
sort(s1, decreasing = T)

#plyr() : 원본 데이터를 분석하기 쉬운 형태로 나누어서 다시 새로운 형태로 만들어주는 패키지
#ply() 앞에 2글자 : 첫 글자 -> 입력될 데이터 유형, 두번째 글자-> 출력될 데이터 유형
#d : dataframe, a : array(matrix 포함), l : list
#ddply(데이터, 기준컬럼, 함수 또는 결과) : dataframe 입력 dataframe 출력
#alply : array 입력 list 출력

install.packages("plyr")
library(plyr)
fruits = read.csv("fruits_10.csv")
fruits

#summarise() : 기준 컬럼의 데이터끼리 모은 후 함수를 적용해서 출력(sql의 group by와 유사)
ddply(fruits, 'name', summarise, sum_qty=sum(qty), sum_price=sum(price))
ddply(fruits, 'name', summarise, max_qty=max(qty), min_price=min(price))
ddply(fruits, c('year', 'name'), summarise, max_qty=max(qty), min_price=min(price))

#transform : 동일한 값의 합계가 아닌 각 행별로 연산을 수행해서 해당 값을 함께 출력
ddply(fruits, 'name', transform, sum_qty=sum(qty), pct_qty=round(qty / sum(qty) * 100, 2))

#dplyr() 패키지
#특징
#1. filter : 조건을 주어서 필터링한다
#2. select : 여러 컬럼이 있는 데이터 셋에서 특정 컬럼만 선택해서 사용
#3. arrange : 데이터들을 오름차순, 내림차순으로 정렬
#4. mutate : 기존의 변수를 활용해서 새로운 변수 생성
#5. summarise : group by. 주어진 데이터를 집계.
#
library(dplyr)
data1 = read.csv("2013년_프로야구선수_성적.csv")
data1
data2 = filter(data1, 경기 >= 120 & 득점 >= 80)
data2
data3 = filter(data1, 포지션%in%c('1루수', '3루수'))
data3

select(data1, 선수명, 포지션, 팀)
select(data1, 순위:타수)
select(data1, -홈런, -타점)
# 여러문장을 조합해서 사용하는 명령어 %>%
data1 %>% select(선수명, 팀, 경기, 타수) %>% filter(타수>=400)
data1 %>% select(선수명, 팀, 경기, 타수) %>% filter(타수 >= 400) %>% arrange(타수)
data1 %>% select(선수명, 팀, 경기, 타수) %>% mutate(경기X타수=경기*타수)
data1 %>% select(선수명, 팀, 경기, 안타, 타수) %>% mutate(타율=round(안타/타수, 3)) %>% arrange(desc(타율))
data1 %>% group_by(팀) %>% summarise(average=mean(경기), na.rm=T)
data1 %>% group_by(팀) %>% summarise_each(mean, 경기, 타수)
data1 %>% group_by(팀) %>% summarise_each(funs(mean, n()), 경기, 타수)

#결측치
#누락된 값, 비어있는 값
#함수 적용 불가, 분석 결과 왜곡
#제거 후 분석 실시

df = data.frame(sex=c('M', 'F', NA, 'M', 'F'),
                score=c(5, 4, 3, 4, NA))
df                                         
is.na(df)
table(is.na(df$sex))
table(is.na(df$score))

mean(df$sex)
df1 = df %>% filter(!is.na(score) & !is.na(sex))
df1
df %>% filter(!is.na(sex))
mean(df1$score)
df2 = na.omit(df)
df2

mean(df$score, na.rm = T)

exam = read.csv("csv_exam.csv")
exam[c(3, 8, 15), 'math'] = NA
exam
exam %>% summarise(mean_math=mean(math, na.rm = T),
                   sum_math=sum(math, na.rm = T),
                   median_math=median(math, na.rm = T))

# 결측치 대체
# 다른 값으로 채워넣기
# 대체법 : 대표값(평균, 최빈값)으로 일괄 대체
# 적용 : 통계분석 기법, 예측값 추정
mean(exam$math, na.rm = T)
exam$math = ifelse(is.na(exam$math), 55, exam$math)
exam
table(is.na(exam$math))

# 이상치 : 정상범주에서 크게 벗어난 값
# 이상치 포함시 분석결과 왜곡
# 이상치를 결측 처리 후 제외하고 분석
# sex : 3, score : 6을 이상치로 가정
df = data.frame(sex=c(1, 2, 1, 3, 2, 1),
                score=c(5, 4, 3, 4, 2, 6))
df
table(df$sex)
table(df$score)

df$sex = ifelse(df$sex == 3, NA, df$sex)
df$score = ifelse(df$score > 5, NA, df$score)
df
df %>% filter(!is.na(sex) & !is.na(score)) %>% group_by(sex) %>% summarise(mean_score=mean(score))
df %>% filter(!is.na(sex) & !is.na(score)) %>% group_by(sex) %>% summarise_each(mean, score)

library(ggplot2)
boxplot(df$sex)
boxplot(df$score)

# 데이터 분석
# 1. 패키지 준비
# 2. 데이터 준비
# 3. 데이터 검토
# 4. 변수명 바꾸기
# 5. 데이터 분석
# 
# 1단계 : 변수 검토 및 전처리
# 2단계 : 변수간 상관관계 분석
#
# 6. 시각화
# 
install.packages('foreign')
library(foreign)
install.packages('readxl')
library(readxl)

wf = read.spss(file = 'Koweps_hpc10_2015_beta1.sav', to.data.frame = T)
wf1 = wf
wf1
head(wf1)
View(wf1)
dim(wf1)
str(wf1)
summary(wf1)
wf1 = rename(wf1, sex=h10_g3,
             birth=h10_g4,
             marriage=h10_g10,
             religion=h10_g11,
             income=p1002_8aq1,
             code_job=h10_eco9,
             code_region=h10_reg7)
class(wf1$sex)
table(wf1$sex)
table(is.na(wf1$sex))

wf1$sex = ifelse(wf1$sex==9, NA, wf1$sex)
wf1$sex = ifelse(wf1$sex==1, 'male', 'female')
table(wf1$sex)
qplot(wf1$sex)

class(wf1$income)
summary(wf1$income)
hist(wf1$income)
qplot(wf1$income) + xlim(0, 1000)
wf1$income=ifelse(wf1$income%in%c(0, 9999), NA, wf1$income)
table(is.na(wf1$income))
sex_in = wf1 %>% filter(!is.na(income)) %>% group_by(sex) %>% summarise(mean_income=mean(income))
sex_in
ggplot(data=sex_in, aes(x=sex, y=mean_income)) + geom_col()

class(wf1$birth)
summary(wf1$birth)
qplot(wf1$birth)
table(is.na(wf1$birth))
wf1$birth = ifelse(wf1$birth == 9999, NA, wf1$birth)
table(is.na(wf1$birth))
wf1$age = 2019 - wf1$birth + 1
summary(wf1$age)
qplot(wf1$age)
age_in = wf1 %>% filter(!is.na(income)) %>% group_by(age) %>% summarise(mean_income=mean(income))
age_in
head(age_in)
ggplot(data = age_in, aes(x=age, y=mean_income)) + geom_line()

install.packages('reshape2')
library(reshape2)

fruits
melt(fruits, id=c('year', 'name')) # wide->long
melt(fruits, id=c('year', 'name'), variable.name = 'var_name', value.name = 'val_name')

mtest = melt(fruits, id=c('year', 'name'), variable.name = 'var_name', value.name = 'val_name')
mtest
dcast(mtest, year + name~var_name) # long->wide
dcast(mtest, year~var_name)

# string() : 작업할 대상 데이터가 문자일 경우
install.packages('stringr')
library(stringr)

#str_detect : 특정 문자가 있는지 탐색
fruits = c('apple', 'Apple', 'banana', 'pineapple')
str_detect(fruits, 'A')
str_detect(fruits, '^a') # 첫 글자가 a인지
str_detect(fruits, 'e$') # 마지막 글자가 e인지
str_detect(fruits, '^[aA]')
str_detect(fruits, '[aA]')

str_detect(fruits, fixed('a', ignore_case = T))

#str_count : 특정 문자 갯수
fruits
str_count(fruits, 'a')
str_count(fruits, fixed('A', ignore_case = T))
str_count(fruits, 'p')

#str_c : 문자열 합치기
str_c('apple', 'pen')
str_c('FRUIT : ', fruits)
str_c(fruits, " is name ", fruits)
str_c(fruits, collapse = ",")

#str_dup : 문자 반복
str_dup(fruits, 3)

#str_length : 문자열 길이
str_length('apple')
str_length(fruits)

#str_locate : 문자열 위치
str_locate('apple', 'a')
str_locate(fruits, 'p')

#str_replace : 문자열 치환
str_replace('apple', 'p', '*')
str_replace_all('apple', 'p', '*')

#str_split : 문자열 자르기
fruits = str_c('apple',',','banana',',','cherry')
fruits
str_split(fruits, ',')

#str_sub : 지정 길이만큼 자르기
str_sub(fruits, start=1, end=3)
str_sub(fruits, start=-7)

#str_trim : 문자열 공백 제거
str_trim('           apple           banana          cherry           ')

library(sqldf)
library(googleVis)
Fruits
sqldf('select * from Fruits')
sqldf("select * from Fruits where Fruit='Apples'")
sqldf("select * from Fruits limit 5")


f1 = function(x) {
  if (x < 0) {
    return(-x)
  }
  else if (x == 0) {
    x = 0
    return(x)
  }
  else {
    x = x * 2
    return(x)
  }
}

f1(-2)
f1(2)
f1(0)

no = scan()
ifelse(no%%2 == 0, '짝수', '홀수')

no = 0
while(no < 5) {
  no = no + 1
  
  if (no == 3) break
  if (no == 2) next
  print(no)
}

f2 = function(x) {
  i = 0
  for (j in 1:x) {
    i = i + j
    print(i)
  }
}
f2(5)

f3 = function(x, y) {
  if (x > 1 && y > 1) {
    z = x * y
  }
  else {
    z = x + y
  }
  return(z)
}

f3(2, 4)
f3(-1, 3)

c1 = c('apple', 'Apple', 'APPLE', 'banana', 'grape')
c2 = c('apple', 'Apple')
grep(c2, c1)
grep(paste(c2, collapse = '|'), c1, value = T) # 값으로 가져오기
grep('^A', c1, value = T)
grep('e$', c1, value = T)
c3 = c('apple1', 'Apple2', 'orange', 'cherry')
grep('[1-9]', c3, value = T)
grep('[[:upper:]]', c3, value = T)

nchar(c1)
nchar('홍길동')
paste('a', 'b', 'c', sep = '@')

substr('abc123', 3, 5)
strsplit('2019/12/27', split = '/')
regexpr('-', '010-1111-2222')

v1 = c(2, 2, 2)
plot(v1)

x = 1:3
y = 3:1

plot(x, y, xlim = c(1, 10), ylim = c(1, 5), xlab = "x축", ylab = "y축", main = "PLOT CHART")

plot.new()

dev.new()
dev.off()

v1 = c(100, 130, 120, 160, 150)
plot(v1, type = 'o', col = 'red', ylim = c(0, 200), axes = F, ann = F)
axis(1, at = 1:5, lab = c("MON", "TUE", "WED", "THU", "FRI"))
axis(2, ylim = c(0, 200))
title(main = "FRUIT", col.main = 'red', font.main = 4)
title(xlab = "DAY", col.lab = 'black')
title(ylab = 'PRICE', col.lab = 'blue')

# 그래프의 배치 조정 : mfrow
# par(mfrow = c(nr, nc))
v1
par(mfrow = c(1, 3))
plot(v1, type = 'o')
plot(v1, type = 's')
plot(v1, type = 'l')
# o :점과 선을 중첩해서
# s : 왼쪽 값을 기초로 계단식
# s : 오른쪽을 기초로 계단식
# p : 점모양
# l : 선 (꺾은 선)
# c : b에서 점을 생략
# h : 각 점에서 x축까지의 수직선
# n : 축만
plot(v1, type = 'p')
plot(v1, type = 'h')
plot(v1, type = 'n')

pie(v1)
plot(v1, type = 'b')
barplot(v1)
par(mfrow = c(1, 1))
par(mfrow = c(1, 3))

a = c(1, 2, 3)
plot(a, xlab = 'aaa')

# mgp=c(제목위치, 지표값 위치, 지표선 위치)
par(mgp = c(0, 1, 0))
# oma(bottom, left, top, right) : 그래프의 전체 여백
par(oma = c(2, 1, 0, 0))

# 여러 개의 그래프를 중첩으로 그림
v1 = c(1, 2, 3, 4, 5)
v2 = c(5, 4, 3, 2, 1)
v3 = c(3, 4, 5, 6, 7)
plot(v1, type = 'o', col = 'red', ylim = c(1, 10))
lines(v2, type = 'l', col = 'blue', ylim = c(1, 5))
lines(v3, type = 's', col = 'green', ylim = c(1, 15))
par(new = T)
plot(v2, type = 'l', col = 'blue', ylim = c(1, 5))
par(new = T)
plot(v3, type = 's', col = 'green')
plot.new()

legend(4, 9, c('v1', 'v2', 'v3'), cex = 0.9, col = c('red', 'blue', 'green'), lty = 1)
# 0 : 투명선 
# 1 : 실선
# 2 : 대시 
# 3 : 점선
# 4 : 점선+대시
# 5 : 긴대시
# 6 : 두개의 대시

x = c(1, 2, 3, 4, 5)
barplot(x, horiz = T)
x = matrix(c(5, 4, 3, 2), 2, 2)
x
barplot(x, beside = T, names = c('1st', '2nd'), col = c('green', 'yellow'), 
        ylim = c(0, 14), xlim = c(0, 14), horiz = T)
par(oma = c(1, 0.5, 1, 0.5))

v1 = c(100, 120, 140, 160, 180)
v2 = c(120, 130, 150, 140, 170)
v3 = c(140, 170, 120, 110, 160)

qty = data.frame(BANANA = v1, CHERRY = v2, ORANGE = v3)
qty
barplot(as.matrix(qty), main = 'FRUITS SALES', beside = T, col = rainbow(nrow(qty)), ylim = c(0, 400))
legend(14, 400, c('MON', 'TUE', 'WED', 'THU', 'FRI'), cex = 0.8, fill = rainbow(nrow(qty)))
# barchart를 그룹으로 묶어 그릴 때는 반드시 출력 대상이 matrix여야 함.
barplot(t(qty), main = 'FRUIT SALES', ylim = c(0, 900), col = rainbow(length(qty)), space = 0.1, cex.axis = 0.8, las = 1, names.arg = c('MON', 'TUE', 'WED', 'THU', 'FRI'), cex = 0.8)

qty
t(qty)

peach = c(180, 200, 250, 198, 170)
colors = c()
for (i in 1:length(peach)) {
  if (peach[i] >= 200) {
    colors = c(colors, 'red')
  }
  else if (peach[i] >= 180) {
    colors = c(colors, 'yellow')
  }
  else {
    colors = c(colors, 'green')
  }
}
barplot(peach, main = 'PEACH', names.arg = c('MON', 'TUE', 'WED', 'THU', 'FRI'), col = colors)

f1 = function(f2) {
  pColor = NULL
  for (i in 1:length(f2)) {
    if (f2[i] >= 200) {
      pColor[i] = 'red'
    }
    else if (f2[i] >= 180) {
      pColor[i] = 'yellow'
    }
    else {
      pColor[i] = 'green'
    }
  }
  return(pColor)
}

f1(peach)
barplot(peach, main = 'PEACH', names.arg = c('MON', 'TUE', 'WED', 'THU', 'FRI'),
        col = f1(peach))

# 히스토그램 : 특정 데이터의 빈도수를 막대그래프로 나타낸 것
h = c(182, 178, 167, 189, 182, 175, 166, 155)
hist(h, main = "히스토그램")

# pie : 전체 합이 100이 되어야 하는 경우. 서로를 비교할 때 적합.
p1 = c(10, 20, 30, 40)
pie(p1, radius = 1, init.angle = 90, col = rainbow(length(p1)), labels = c('week1', 'week2', 'week3', 'week4'))
pct = p1 / sum(p1) * 100
lab1 = c('week1', 'week2', 'week3', 'week4')
lab = paste(lab1, "\n", pct, " %")
pie(p1, radius = 1, init.angle = 90, col = rainbow(length(p1)), labels = lab)
# legend(1, 1.1, lab1, cex = 0.8, fill = rainbow(length(p1)))

install.packages('plotrix')
library(plotrix)

p1 = c(10, 20, 30, 40)
pct = p1 / sum(p1) * 100
lab1 = c('week1', 'week2', 'week3', 'week4')
lab = paste(lab1, '\n', pct, ' %')
pie3D(p1, main = '3D PIE', col = rainbow(length(p1)), cex = 0.5, labels = lab, explode = 0.05)

# 상자 차트(boxplot)(최대, 최소, 중앙값)
v1 = c(10, 12, 15, 11, 20)
v2 = c(5, 7, 15, 8, 9)
v3 = c(11, 20, 15, 18, 13)
boxplot(v1, v2, v3, col = c('blue', 'pink', 'yellow'), horizontal = T, names = c('BLUE', 'PINK', 'YELLOW'))

# 관계도(igraph)
install.packages('igraph')
library(igraph)

g1 = graph(c(1, 2, 2, 3, 2, 4, 1, 4, 5, 5, 3, 6), directed = T)
plot(g1)

print_all(g1)
name = c('홍길동 대표', '일지매 부장', '김유신 과장', '손흥민 대리', '노홍철 대리', '이순신 부장', '유관순 과장', '강감찬 부장', '신사임당 대리', '광개토 과장', '정몽주 대리')
pemp = c('홍길동 대표', '홍길동 대표', '일지매 부장', '김유신 과장', '김유신 과장', '홍길동 대표', '이순신 부장', '유관순 과장', '홍길동 대표', '강감찬 부장', '광개토 과장')
emp = data.frame(이름=name, 상사=pemp)
emp

g = graph.data.frame(emp, directed = T)
plot(g, layout = layout.fruchterman.reingold, vertex.size = 8, edge.arrow.size = 0.5)#, vertex.label = NA)
dev.new()
savePlot('network_3.png', type = 'jpg')


install.packages('devtools')
library(devtools)

install_github('christophergandrud/d3Network')
install.packages('RCurl')
library(d3Network)
library(RCurl)

name = c('홍길동 대표', '일지매 부장', '김유신 과장', '손흥민 대리', '노홍철 대리', '이순신 부장', '유관순 과장', '강감찬 부장', '신사임당 대리', '광개토 과장', '정몽주 대리')
pemp = c('홍길동 대표', '홍길동 대표', '일지매 부장', '김유신 과장', '김유신 과장', '홍길동 대표', '이순신 부장', '유관순 과장', '홍길동 대표', '강감찬 부장', '광개토 과장')
emp = data.frame(이름=name, 상사=pemp)
emp
d3SimpleNetwork(emp, width = 600, height = 600, file = "C:/Users/user/Desktop/Youngmin/KW/Programming_Practice/R/R_data/d3.html")


# 군집 분석 : 데이터를 여러 집단으로 나눈 후 특성 및 차이 분석
g = read.csv("군집분석.csv", header = T)
g1 = data.frame(학생=g$학생, 교수=g$교수)
plot(g1, layout = layout.fruchterman.reingold, vertex.size = 2, edge.arrow.size = 0.1, vertex.color = 'green', vertex.label = NA)
plot(g1, layout = layout.kamada.kawai, vertex.size = 2, edge.arrow.size = 0.1, vertex.color = 'green', vertex.label = NA)

g2 = graph.data.frame(g1, directed = T)
g2
V(g2)$name

gubun1 = V(g2)$name
library(stringr)
gubun = str_sub(gubun1, start = 1, end = 1)
gubun

colors = c()
for (i in 1:length(gubun)) {
  if (gubun[i] == 'S') {
    colors = c(colors, 'red')
  }
  else
    colors = c(colors, 'green')
}

sizes = c()
for (i in 1:length(gubun)) {
  if (gubun[i] == 'S') {
    sizes = c(sizes, 6)
  }
  else
    sizes = c(sizes, 6)
}

plot(g2, layout = layout.kamada.kawai, vertex.size = sizes, edge.arrow.size = 0.1, vertex.color = colors, vertex.label = NA)

# 학생과 교수의 도형을 학생은 circle, 교수는 square로
shapes = c()
for (i in 1:length(gubun)) {
  if (gubun[i] == 'S') {
    shapes = c(shapes, 'circle')
  }
  else
    shapes = c(shapes, 'square')
}
plot(g2, layout = layout.kamada.kawai, vertex.size = sizes, vertex.shape = shapes, edge.arrow.size = 0.1, vertex.color = colors, vertex.label = NA)

total = read.csv("학생별전체성적_new.txt", sep = ',')
total
row.names(total) = total$이름
total = total[,2:7]
total

stars(total, flip.labels = F, draw.segment = F, frame.plot = T, full = T, main = '학생 과목별 성적')
lab = names(total)
value = table(lab)
value
pie(value, label = lab, radius = 0.1, cex = 0.6, col = NA)
dev.new()
savePlot("star+2.jpg", type = 'jpg')

stars(total, flip.labels = F, draw.segment = T, frame.plot = T, full = T, main = '학생 과목별 성적', key.loc = c(0.2, 6.5), key.xpd = F)

# radarchart
# 1. 샘플데이터 생성
# 2. 최대값, 최소값
# 3. radarchart
install.packages('fmsb')
library(fmsb)
layout = data.frame(
  분석력 = c(5, 1),
  창의력 = c(15, 3),
  판단력 = c(3, 0),
  리더쉽 = c(5, 1),
  사교성 = c(5, 1))
set.seed(123)
data1 = data.frame(
  분석력 = runif(3, 1, 5), # 균등 분포
  창의력 = rnorm(3, 10, 2), # 정규 분포(갯수, 평균, 표준편차)
  판단력 = c(0.5, NA, 3),
  리더쉽 = runif(3, 1, 5),
  사교성 = c(5, 2.5, 4)
)
data2 = rbind(layout, data1)
op = par(oma = c(1, 0.5, 3, 1), mfrow = c(2, 2))
radarchart(data2, axistype = 1, seg = 5, plty = 1, title = '1st')
radarchart(data2, axistype = 2, pcol = topo.colors(3), plty = 1, title = '2nd')
radarchart(data2, axistype = 3, pty = 32, plty = 1, axislabcol = 'grey', title = '3rd')
radarchart(data2, axistype = 0, plwd = 1:5, pcol = 1, title = '4th')

# 저수준 작도
# 점 : point()
# 직선 : lines(), segment(), abline()
# 격자 : grid()
# 화살표 : arrows()
# 직사각형 : rect()
# 문자 : text(), mtext(), title()
# 테두리, 축 : box(), axis()
# 범례 : legend()
# 다각형 : polygon()
par(mfrow = c(1, 1))
plot(1:15)
abline(h = 8)
rect(1, 6, 3, 8)
arrows(1, 1, 5, 5)
text(8, 9, 'TEXT')
title('TEST TITLE')

library(ggplot2)
ko = read.table('학생별국어성적_new.txt', header = T, sep = ',')
ko
ggplot(ko, aes(x = 이름, y = 점수)) + geom_point()
# ggplot(dataframe, aes(x = x축 데이터, y = y축 데이터)) + geom_func()
# geom() 설정값
# - stat : 주어진 데이터에서 geom에 필요한 데이터를 생성한다.
# - stat_bin : 
#   - count : 각 항목의 빈도수
#   - density : 각 항목의 밀도수
#   - ncount : 값의 범위 (0, 1)로 스케일링
#   - ndensity : 값의 범위가 (0, 1)로 스케일링
#   - 위 설정 값을 지정하지 않으면 기본 값은 count

gg = ggplot(ko, aes(x = 이름, y = 점수)) + geom_bar(stat = 'identity', fill = 'green', color = 'red')

# theme는 ggplot2에 주로 글자와 관련된 기능
gg + theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust = 1, color = 'blue', size = 8))

kem = read.csv('학생별과목별성적_국영수_new.csv', header = T)
kem

library(plyr)
sort_kem = arrange(kem, 이름, 과목)
sort_kem
s_kem = ddply(sort_kem, "이름", transform, 누적합계=cumsum(점수))
s_kem
ss_kem = ddply(s_kem, "이름", transform, 누적합계=cumsum(점수), label = cumsum(점수) - 0.5 * 점수)
ss_kem

ggplot(ss_kem, aes(x = 이름, y = 점수, fill = 과목)) + geom_bar(stat = 'identity', position = position_stack(reverse = T)) + geom_text(aes(y = label, label = paste(점수, ' 점')), color = 'black', size = 4) + guides(fill = guide_legend(reverse = T))


# geom_segment() : 클리블랜드 점 그래프
score = read.table('학생별전체성적_new.txt', header = T, sep = ",")
score                                                          
class(score)
score[, c("이름", "영어")]
gg = ggplot(score, aes(x = 영어, y = reorder(이름, 영어)))
gg = gg + geom_point(size = 4, color = 'green') + theme_bw() + theme(panel.grid.major.x = element_blank(), panel.grid.major.y = element_line(colour = 'red', linetype = 'dashed'), panel.grid.minor.x = element_blank())
gg + geom_segment(aes(yend = 이름), xend = 0, color = 'blue') + theme(panel.grid.major.y = element_blank())                                               


# geom_point()
install.packages('gridExtra')
library(gridExtra)

vmt = mtcars
vmt

g1 = ggplot(vmt, aes(x = hp, y = mpg))
g1 + geom_point(aes(color = factor(am), size = wt, shape = factor(am))) + scale_color_manual(values = c('red', 'green'))

g2 = g1 + geom_point(color = 'red') + geom_line() + labs(x='마력',y='연비')
g2

th = read.csv('학생별과목별성적_3기_3명.csv', header = T, sep = ',')
th
ss = arrange(th, 이름, 과목)
ss
ggplot(ss, aes(x = 과목, y = 점수, color = 이름, group = 이름)) + geom_line() + geom_point(size = 6, shape = 17) # shape 0 ~ 25까지 있음.

dis = read.csv('1군전염병발병현황_년도별.csv', stringsAsFactors = F)
dis
ggplot(dis, aes(x = 년도별, y = 장티푸스, group = 1)) + geom_line()
ggplot(dis, aes(x = 년도별, y = 장티푸스, group = 1)) + geom_area(color = 'red', fill = 'cyan', alpha = 0.4) + geom_line()


# 워드클라우드
# 1. 데이터에서 단어만 추출
# 2. 단어집합 생성
# 3. 단어 필터링
# 4. 단어 핸들링
# 5. txt 파일로 저장하고 table로 읽어들이면서 공백제거
# 6. 단어 빈도수 저장
# 7. wordcloud 출력
# ※ 자바로딩이 안될 경우
#   Sys.setenv(JAVA_HOME=jre 경로\bin)

install.packages('KoNLP')
install.packages('wordcloud')
library(KoNLP)
library(wordcloud)

install.packages('RColorBrewer')
library(dplyr)
library(plyr)
library(RColorBrewer)

useSejongDic()
data1 = readLines('BTS유엔연설_국문.txt')
data1

# 1. 데이터에서 단어만 추출
data2 = sapply(data1, extractNoun, USE.NAMES = F)
data2

head(unlist(data2), 30) # unlist : 리스트를 벡터로 변환

# 2. 단어집합 생성
data3 = unlist(data2)
data3

# 3. 단어 필터링 gsub(변경 전 글자, 변경 후 글자, 원본 데이터)
data3 = gsub('\\d+', '', data3)
data3 = gsub('[저|내]', '나', data3)
data3 = gsub('[하게|해서|돌|-|것|]', '', data3)
data3 = gsub(' ', '', data3)
data3
# 4. 단어 핸들링

# 5. txt 파일로 저장하고 table로 읽어들이면서 공백 제거
write(unlist(data3), 'BTS_국.txt')
data4 = read.table('BTS_국.txt')
data4
nrow(data4)

# 6. 단어 빈도수 저장
wc = table(data4)
wc
head(sort(wc, decreasing = T), 20)

# 7. wordcloud 출력
pal = brewer.pal(9, 'Set3')
wordcloud(names(wc), freq = wc, scale = c(5, 1), rot.per = 0.25, min.freq = 1, random.order = F, random.color = T, colors = pal)
legend(0.3, 1, 'BTS유엔 연설문', cex = 0.8, fill = NA, border = NA, bg = 'white', text.col = 'red', text.font = 2, box.col = 'red')


# 191231
library(dplyr)
library(plyr)
library(ggplot2)
library(lubridate)
library(stringr)
library(devtools)
library(RColorBrewer)
library(foreign)
library(googleVis)
library(KoNLP)
library(wordcloud)

useSejongDic()

# 1. 데이터에서 단어 추출
data1 = readLines("remake.txt")
data1
data2 = sapply(data1, extractNoun, USE.NAMES = F)
data2

# 2. 단어집합 생성
data3 = unlist(data2)
data3

# 3. 단어 필터링
data3 = Filter(function(x) {
  nchar(x) <= 10
}, data3)
data3

data3 = gsub('\\d+', '', data3)
data3 = gsub('(쌍수|쌍커풀)', '쌍꺼풀', data3)
data3 = gsub('메부리코', '매부리코', data3)
data3 = gsub(' ', '', data3)
data3 = gsub('\\.', '', data3)
data3 = gsub("\\'", '', data3)
data3 = gsub('수', '', data3)
data3

write(unlist(data3), 'remake_2.txt')
data4 = read.table('remake_2.txt')
data4
nrow(data4)

wc = table(data4)
wc
head(sort(wc, decreasing = T), 20)
txt = readLines('성형gsub.txt')
txt
cnttxt = length(txt)
cnttxt
i = 1
for (i in 1:cnttxt) {
  data3 = gsub(txt[i], '', data3)
}
data3
data3 = Filter(function(x) {
  nchar(x) >= 2
}, data3)
write(unlist(data3), 'remake_2.txt')
data4 = read.table('remake_2.txt')
data4

wc = table(data4)
wc
head(sort(wc, decreasing = T), 20)

pal = brewer.pal(8, 'Set2')
wordcloud(names(wc), freq = wc, scale = c(5, 1), rot.per = 0.25, min.freq = 2, random.order = F, random.color = T, colors = pal)

txt = readLines('jeju.txt')
place = sapply(txt, extractNoun, USE.NAMES = F)
place

head(unlist(place), 30)
cdata = unlist(place)
place = str_replace_all(cdata, '[^[:alpha:]]', '')
place = gsub(' ', '', place)
txt = readLines('제주도여행코스gsub.txt')
txt
cnt = length(txt)
cnt
i = 1
for (i in 1:cnt) {
  place = gsub(txt[i], '', place)
}
place
place = Filter(function(x) {
  nchar(x) >= 2
}, place)
write(unlist(place), 'jeju_2.txt')
rev = read.table('jeju_2.txt')
rev
nrow(rev)
wc = table(rev)
wc
head(sort(wc, decreasing = T), 30)

mergeUserDic(data.frame(readLines('제주도여행지.txt'), 'ncn'))

pal = brewer.pal(9, 'Set3')
wordcloud(names(wc), freq = wc, scale = c(5, 1), rot.par = 0.25, min.freq = 2, random.order = F, random.color = T, colors = pal)

# seoul_go.txt 파일을 이용하여 서울 명소들을 워드 클라우드로 생성
mergeUserDic(data.frame(readLines('서울명소merge.txt'), 'ncn'))

seoul = readLines('seoul_go.txt')
seoul
seoul2 = sapply(seoul, extractNoun, USE.NAMES = F)
seoul2
seoul3 = unlist(seoul2)
seoul3
seoul3 = Filter(function(x) {
  nchar(x) >= 2
}, seoul3)
seoul3

filter = readLines('서울명소gsub.txt')
cnt = length(filter)
i = 1
for (i in 1:cnt) {
  seoul3 = gsub(filter[i], '', seoul3)
}
seoul3

seoul3 = gsub('\\d+', '', seoul3)
seoul3 = gsub('[^[:alpha:]]', '', seoul3)
seoul3 = gsub('\\.', '', seoul3)
seoul3 = gsub('(//|~)', '', seoul3)
seoul3 = gsub('(북촌|북촌한옥)', '북촌한옥마을', seoul3)
seoul3 = gsub('인사', '인사동', seoul3)

seoul3 = Filter(function(x) {
  nchar(x) >= 2
}, seoul3)
write(unlist(seoul3), 'seoul_2.txt')
seoul4 = read.table('seoul_2.txt')
seoul4
wc = table(seoul4)
wc
head(sort(wc, decreasing = T), 40)

dev.new()
wordcloud(names(wc), freq = wc, scale = c(5, 1), rot.par = 0.25, min.freq = 2, random.order = F, random.color = T, colors = pal)


install.packages('tm')
library(tm)
data1 = readLines('steve.txt')

# 말뭉치
corp1 = VCorpus(VectorSource(data1))
corp1

inspect(corp1)

tdm = TermDocumentMatrix(corp1)
tdm

m = as.matrix(tdm)
m

corp2 = tm_map(corp1, stripWhitespace) # 여러 개의 공백을 하나로 치환
corp2 = tm_map(corp2, tolower)
corp2 = tm_map(corp2, removeNumbers)
corp2 = tm_map(corp2, removePunctuation) # .,:; 제거
corp2 = tm_map(corp2, PlainTextDocument) # 일반문서로 변환

sword2 = c(stopwords('en'), 'and', 'but', 'not')
# content_transformer(tolower)
corp2 = tm_map(corp2, removeWords, sword2)
tdm2 = TermDocumentMatrix(corp2)
m2 = as.matrix(tdm2)
m2
class(m2)
colnames(m2) = c(1:59)

freq1 = sort(rowSums(m2), decreasing = T)
head(freq1)
freq2 = sort(colSums(m2), decreasing = T)
head(freq2, 20)
findFreqTerms(tdm2, 2)
findAssocs(tdm2, 'apple', 0.5)
pal = brewer.pal(7, 'Set3')
wordcloud(names(freq1), freq = freq1, scale = c(5, 1), min.freq = 1, colors = pal, random.order = F, random.color = T)



data1 = readLines('BTS유엔연설_영문.txt')
data1

# 말뭉치
corp1 = VCorpus(VectorSource(data1))
corp1

inspect(corp1)

tdm = TermDocumentMatrix(corp1)
tdm

m = as.matrix(tdm)
m

corp2 = tm_map(corp1, stripWhitespace) # 여러 개의 공백을 하나로 치환
corp2 = tm_map(corp2, tolower)
corp2 = tm_map(corp2, removeNumbers)
corp2 = tm_map(corp2, removePunctuation) # .,:; 제거
corp2 = tm_map(corp2, PlainTextDocument) # 일반문서로 변환

sword2 = c(stopwords('en'), 'and', 'but', 'not')
# content_transformer(tolower)
corp2 = tm_map(corp2, removeWords, sword2)
tdm2 = TermDocumentMatrix(corp2)
m2 = as.matrix(tdm2)
m2
class(m2)
colnames(m2) = c(1:31)

freq1 = sort(rowSums(m2), decreasing = T)
wc_freq1 = head(freq1, 10)
freq2 = sort(colSums(m2), decreasing = T)
head(freq2, 20)
findFreqTerms(tdm2, 2)
findAssocs(tdm2, 'bts', 0.5)
pal = brewer.pal(7, 'Set3')
wordcloud(names(freq1), freq = freq1, scale = c(5, 1), min.freq = 1, colors = pal, random.order = F, random.color = T)

barplot(wc_freq1)


# 제주도 추천 여행지
top10 = head(sort(wc, decreasing = T), 10)
top10
pct = round(top10 / sum(top10) * 100, 1)
names(top10)
lab = paste(names(top10), "\n", pct, ' %')
pie(top10, main = "제주도 추천 여행지 top10", col = rainbow(10), radius = 1, cex = 1.2, labels = lab)

bchart = head(sort(wc, decreasing = T), 10)
bp = barplot(bchart, main = "제주도 추천 여행지 top10", col = rainbow(10), cex.names = 1.2, las = 2, ylim = c(0, 20))
text(x = bp, y = bchart * 1.05, labels = paste('(', pct, '%', ')'), col = 'black', cex = 1)
text(x = bp, y = bchart * 0.95, labels = paste(bchart, '건'), col = 'black', cex = 1)

bchart2 = rev(bchart)
bp = barplot(bchart2, main = "제주도 추천 여행지 top10", col = rainbow(10), cex.names = 1.2, las = 2, ylim = c(0, 20))
text(x = bp, y = bchart2 * 1.05, labels = paste('(', pct, '%', ')'), col = 'black', cex = 1)
text(x = bp, y = bchart2 * 0.95, labels = paste(bchart2, '건'), col = 'black', cex = 1)

barplot(bchart, main = "제주도 추천 여행지 top10", col = rainbow(10), xlim = c(0, 25), cex.name = 1, horiz = T)
text(y = bp, x = bchart * 0.9, labels = paste('(', pct, '%', ')'), col = 'black', cex = 1)
text(y = bp, x = bchart * 1.15, labels = paste(bchart, '건'), col = 'black', cex = 1)

library(plotrix)
pie3D(bchart, main = '제주도 추천 여행지 top10', col = rainbow(10), cex = 0.5, labels = lab, explode = 0.05)


propose_data = readLines('propose.txt')
propose_data

propose_data_apply = sapply(propose_data, extractNoun, USE.NAMES = F)
propose_data_apply
propose_unlist = unlist(propose_data_apply)
propose_unlist

propose_unlist = Filter(function(x) {
  nchar(x) >= 2
}, propose_unlist)

filter = readLines('proposegsub.txt')
cnt = length(filter)
i = 1
for (i in 1:cnt) {
  propose_unlist = gsub(filter[i], '', propose_unlist)
}

propose_filter = gsub('\\d+', '', propose_unlist)
propose_filter
propose_filter = gsub('\\.', '', propose_filter)

propose_filter = Filter(function(x) {
  nchar(x) >= 2
}, propose_filter)
write(unlist(propose_filter), 'propose_present.txt')
present = read.table('propose_present.txt')
present
wc = table(present)
bchart = head(sort(wc, decreasing = T), 10)

colors = c()
for (i in 1:length(bchart)) {
  if (bchart[i] >= 50) {
    colors = c(colors, 'red')
  }
  else if (bchart[i] >= 30) {
    colors = c(colors, 'yellow')
  }
  else if (bchart[i] >= 10) {
    colors = c(colors, 'blue')
  }
  else
    colors = c(colors, 'pink')
}

par(mfrow = c(2, 2))

bp = barplot(bchart, main = "프로포즈 top10", col = colors, cex.names = 1, ylim = c(0, 60), las = 2)
text(x = bp, y = bchart + 4, labels = paste(bchart, ' 건'), col = 'black', cex = 1.0)

present_top10 = round(bchart / sum(bchart) * 100, 1)
present_top10
lab = paste(names(present_top10), '\n', present_top10, ' %')
pie(present_top10, main = "프로포즈 top10", col = colors, radius = 1, cex = 0.8, labels = lab)

pal = brewer.pal(7, 'Set3')
wordcloud(names(wc), freq = wc, scale = c(5, 1), min.freq = 1, random.order = F, random.color = T, colors = pal)
legend('top', '프로포즈 top10', cex = 0.8, fill = NA, border = NA, bg = 'white', text.col = 'red', text.font = 2, box.col = 'red')

pie3D(present_top10, main = "프로포즈 top10", col = colors, cex = 0.8, labels = lab, labelcex = 0.7, explode = 0.05)
