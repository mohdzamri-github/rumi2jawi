# rumi2jawi
rumi2jawi using gcloud and python 3 . similar code to rumi-to-jawi

make sure to run gcloud init before launch
gunicorn

```
gcloud init
<select account and project>
gunicorn -b :8090 --reload --max-requests 1 main:app
```



*better unicode support*

*gcloud app deploy*


