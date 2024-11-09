#!/bin/bash

# 정책 ARN 설정
policy_arn="arn:aws:iam::003728344779:policy/cwuserpolicy1"
policy_arn1="arn:aws:iam::003728344779:policy/validatepolicy1"
#policy_arn2="arn:aws:iam::003728344779:policy/cwiamuserself_policy1"

# JSON 파일 읽기
users=$(cat user_list.json | jq -c '.[]')

# 각 사용자에게 정책 추가
for user in $users; do
    user_name=$(echo $user | jq -r '.UserName')

aws iam attach-user-policy --user-name "$user_name" --policy-arn "$policy_arn"
    echo "Attaching policy to user: $user_name"
    aws iam attach-user-policy --user-name "$user_name" --policy-arn "$policy_arn"
    aws iam attach-user-policy --user-name "$user_name" --policy-arn "$policy_arn1"
    #aws iam attach-user-policy --user-name "$user_name" --policy-arn "$policy_arn2"
done
