#### 기본적인 BFS 동작 흐름
- 1. 시작하는 칸을 큐에 넣고 방문했다는 표시를 남김
- 2. 큐에서 원소를 꺼내어 그 칸에 상하좌우로 인접한 칸에 대해 3번을 진행
- 3. 해당 칸을 이전에 방문했다면 아무것도 하지 않음
- 3. 처음으로 방문했다면 방문했다는 표시를 남기고 해당 칸을 큐에 삽입
- 4. 큐가 빌 때까지 반복
- 모든 칸이 큐에 1번씩 들어가므로 시간 복잡도는 칸이 N개일 때 O(N)




