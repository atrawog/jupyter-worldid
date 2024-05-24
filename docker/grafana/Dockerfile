# Use an official Grafana image as the base
FROM grafana/grafana:latest

# Switch to root to install packages and set up the environment
USER root

# Install curl to fetch dashboard JSON files
RUN apk update && apk add --no-cache curl \
    && mkdir -p /var/lib/grafana/dashboards

# Download dashboard JSON files
RUN curl -o /var/lib/grafana/dashboards/dashboard_1860.json https://grafana.com/api/dashboards/1860/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_11670.json https://grafana.com/api/dashboards/11670/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_14282.json https://grafana.com/api/dashboards/14282/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_893.json https://grafana.com/api/dashboards/893/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_395.json https://grafana.com/api/dashboards/395/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_609.json https://grafana.com/api/dashboards/609/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_4271.json https://grafana.com/api/dashboards/4271/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_11670.json https://grafana.com/api/dashboards/11670/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_13946.json https://grafana.com/api/dashboards/13946/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_15894.json https://grafana.com/api/dashboards/15894/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_19908.json https://grafana.com/api/dashboards/19908/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_19792.json https://grafana.com/api/dashboards/19792/revisions/latest/download \    
    && curl -o /var/lib/grafana/dashboards/dashboard_12831.json https://grafana.com/api/dashboards/12831/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_14841.json https://grafana.com/api/dashboards/14841/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_13496.json https://grafana.com/api/dashboards/13496/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_12486.json https://grafana.com/api/dashboards/12486/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_10619.json https://grafana.com/api/dashboards/10619/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_11600.json https://grafana.com/api/dashboards/11600/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_4271.json https://grafana.com/api/dashboards/4271/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_5763.json https://grafana.com/api/dashboards/5763/revisions/latest/download \
    && curl -o /var/lib/grafana/dashboards/dashboard_13496.json https://grafana.com/api/dashboards/13496/revisions/latest/download

# Add provisioning configuration for dashboards and set ownership
COPY --chown=grafana:grafana dashboards.yml /etc/grafana/provisioning/dashboards/dashboards.yml

# Add provisioning configuration for data sources and set ownership (optional, but usually needed)
COPY --chown=grafana:grafana datasources.yml /etc/grafana/provisioning/datasources/datasources.yml

# Ensure Grafana uses the custom configuration
RUN chmod -R 644 /etc/grafana/provisioning/dashboards/dashboards.yml \
    && chmod -R 644 /etc/grafana/provisioning/datasources/datasources.yml

# Expose Grafana port
EXPOSE 3000

# Switch back to the Grafana user
USER grafana

# Start Grafana
CMD ["/run.sh"]
