#!/bin/bash
GITHUB_REPO="Nagarajcts/Jmeterui"  
GITHUB_TOKEN="2CX6PgUlPZrdv3vEtK75Q6tZ9yF3fk3qy7cG"    
GITHUB_WORKFLOW="jmeterui.yml"      
REF="main"                             

# Trigger GitHub Action via GitHub API
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  -H "Authorization: Bearer ghp_$GITHUB_TOKEN" \
  https://api.github.com/repos/$GITHUB_REPO/actions/workflows/$GITHUB_WORKFLOW/dispatches \
