#!/bin/bash
read -p "Commit: " desc
git add . && \
git add -u && \
git commit -m "$desc" && \
git push origin HEAD