#!/bin/bash

# 초기 비밀번호 설정
initial_password="Iam@1234"

# JSON 파일 읽기
users=$(cat user_list.json | jq -c '.[]')

# 각 사용자에 대해 비밀번호 설정
for user in $users; do
    user_name=$(echo $user | jq -r '.UserName')

    echo "Setting password for user: $user_name"

    # 사용자의 로그인 프로필 생성 및 초기 비밀번호 설정 (비밀번호 변경 강제 안함)
    aws iam create-login-profile --user-name "$user_name" \
        --password "$initial_password"
done
