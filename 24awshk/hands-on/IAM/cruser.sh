#!/bin/bash

# JSON 파일 읽기
users=$(cat user_list.json | jq -c '.[]')

# 각 사용자 생성
for user in $users; do
    user_name=$(echo $user | jq -r '.UserName')

    echo "Creating user: $user_name"
    aws iam create-user --user-name "$user_name"

    # 필요 시 사용자에게 정책 또는 그룹 추가
    # aws iam attach-user-policy --user-name "$user_name" --policy-arn "arn:aws:iam::aws:policy/YourPolicyArn"
    # aws iam add-user-to-group --user-name "$user_name" --group-name "YourGroupName"
done
