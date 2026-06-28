# Use the official public ERPNext base image
FROM frappe/erpnext:v15.0.0

# Set the working directory
WORKDIR /home/frappe/frappe-bench

# Expose ERPNext web service port
EXPOSE 8000

# Start command
CMD ["bench", "start"]
