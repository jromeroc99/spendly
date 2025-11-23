FROM python:3.12 AS builder

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
RUN reflex export --frontend-only --no-zip
RUN ls -l /app/.web || true
RUN ls -l /app || true


FROM nginx

COPY --from=builder /app/.web/build/client /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf