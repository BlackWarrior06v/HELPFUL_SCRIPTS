#!/bin/bash

# Variables de configuración
REMOTE_USER="curi"
REMOTE_HOST="148.216.53.218"
REMOTE_DIRS=("Fluctuations6" "Fluctuations8" "Fluctuations85" "Fluctuations9" "Fluctuations95" "Fluctuations10" "Fluctuations15" "Fluctuations20" "Fluctuations25" "Fluctuations30")
LOCAL_DIRS=("vc6" "vc8" "vc85" "vc9" "vc95" "vc10" "vc15" "vc20" "vc25" "vc30")
FILE_NAME="M.t.asc"
LOCAL_BASE_DIR="/home/curi99/IFM/BlackHole_Gpp/Fluctuations/NO_BH"
REMOTE_BASE_DIR="/home/curi/BlackHole_Fluctuations"

# Descargar archivos usando scp
for i in "${!REMOTE_DIRS[@]}"; do
  REMOTE_DIR="${REMOTE_DIRS[$i]}"
  LOCAL_DIR="${LOCAL_DIRS[$i]}"

  scp "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_BASE_DIR}/${REMOTE_DIR}/${FILE_NAME}" "${LOCAL_BASE_DIR}/${LOCAL_DIR}/"
done
