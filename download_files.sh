#!/bin/bash

# Variables de configuración
REMOTE_USER="user"
REMOTE_HOST="IP"
REMOTE_DIRS=("remotesdir")
LOCAL_DIRS=("localsdirs")
LOCAL_BASE_DIR="localbasedir"
REMOTE_BASE_DIR="remotebasedir"
FILE_NAMES=("bunchoffilenames")

# Descargar archivos usando scp

# Par file
for i in "${!REMOTE_DIRS[@]}"; do
  REMOTE_DIR="${REMOTE_DIRS[$i]}"
  LOCAL_DIR="${LOCAL_DIRS[$i]}"

  scp "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_BASE_DIR}/${REMOTE_DIR}.par" "${LOCAL_BASE_DIR}/${LOCAL_DIR}/"
done

for j in "${!FILE_NAMES[@]}"; do
  FILE_NAME="${FILE_NAMES[$j]}"
  # Descargar archivos usando scp  
  for i in "${!REMOTE_DIRS[@]}"; do
    REMOTE_DIR="${REMOTE_DIRS[$i]}"
    LOCAL_DIR="${LOCAL_DIRS[$i]}"

    scp "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_BASE_DIR}/${REMOTE_DIR}/${FILE_NAME}" "${LOCAL_BASE_DIR}/${LOCAL_DIR}/"
  done
done
