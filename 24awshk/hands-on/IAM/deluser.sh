#!/bin/bash

# JSON 파일 읽기
users=$(cat user_list.json | jq -c '.[]')

# 각 사용자 삭제
for user in $users; do
    user_name=$(echo $user | jq -r '.UserName')

    echo "Deleting user: $user_name"

    # 사용자에게 연결된 정책을 먼저 분리
    aws iam list-attached-user-policies --user-name "$user_name" | jq -r '.AttachedPolicies[].PolicyArn' | while read policy_arn; do
        echo "Detaching policy: $policy_arn from user: $user_name"
        aws iam detach-user-policy --user-name "$user_name" --policy-arn "$policy_arn"
    done

    # 사용자 그룹에서 제거
    aws iam list-groups-for-user --user-name "$user_name" | jq -r '.Groups[].GroupName' | while read group_name; do
        echo "Removing user: $user_name from group: $group_name"
        aws iam remove-user-from-group --user-name "$user_name" --group-name "$group_name"
    done

    # 로그인 프로필 삭제 (비밀번호가 설정되어 있다면)
    aws iam delete-login-profile --user-name "$user_name" 2>/dev/null

    # 사용자 삭제
    aws iam delete-user --user-name "$user_name"
done
