# Define the environment name
STREAMLIT_PID = .streamlit_pid

# Phony targets
.PHONY: run stop

# Command to run the Streamlit app
run:
	streamlit run app.py & echo $$! > $(STREAMLIT_PID)
	@echo "Streamlit is running on http://localhost:8501"

# Command to stop the Streamlit app
stop:
	@if [ -f $(STREAMLIT_PID) ]; then \
		PID=$$(cat $(STREAMLIT_PID)); \
		kill $$PID && rm $(STREAMLIT_PID) && echo "Stopping Streamlit..."; \
		sleep 1; \
		if ps -p $$PID > /dev/null; then \
			echo "Force stopping Streamlit..."; \
			kill -9 $$PID; \
		fi; \
		echo "Streamlit has been stopped."; \
	else \
		echo "Streamlit is not running or PID file not found."; \
	fi