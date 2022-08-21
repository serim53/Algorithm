package com.ssafy.ws01.step3;

import java.util.Scanner;

public class GameTest {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int user_win = 0;	// 유저가 이긴 횟수
		int com_win = 0;	// 컴퓨터가 이긴 횟수
		int win_num = 0;	// 승리를 위해 이겨야 하는 횟수
		int game_cnt = 0;	// 전체 게임 횟수
	 	int now_game_cnt = 0;	// 현재 게임 횟수
		
		System.out.println("가위바위보 게임을 시작합니다. 아래 보기 중 하나를 고르세요.");
		System.out.println("1. 5판 3승");
		System.out.println("2. 3판 2승");
		System.out.println("3. 1판 1승");
		System.out.print("번호를 입력하세요. ");
		
		int game = scan.nextInt();
		
		// 1번 게임 선택 => 5판 3승제
		if (game == 1) {
			win_num = 3;
			game_cnt = 5;
		}
		// 2번 게임 선택 => 3판 2승제
		if (game == 2) {
			win_num = 2;
			game_cnt = 3;
		}
		// 3번 게임 선택 => 1판 1승제
		if (game == 3) {
			win_num = 1;
			game_cnt = 1;
		}
		
		do {
			System.out.print("가위바위보 중 하나 입력: ");
			String user = scan.next();	// 유저가 낸 것
			int com = (int)(Math.random() * 3) + 1;	// 컴퓨터가 낸 것
			// 현재 게임 횟수 1 증가
			now_game_cnt += 1;
			// 1: 바위, 2: 보, 3: 가위
			if(user.equals("가위")) {
				if(com == 1) {
					System.out.print("졌습니다!!!");
					com_win += 1;
				}
				if(com == 2) {
					System.out.print("이겼습니다!!!");
					user_win += 1;
				}
				if(com == 3) {
					System.out.print("비겼습니다!!!");
				}
				System.out.println();
			}
			if(user.equals("바위")) {
				if(com == 1) {
					System.out.print("비겼습니다!!!");
				}
				if(com == 2) {
					System.out.print("졌습니다!!!");
					com_win += 1;
				}
				if(com == 3) {
					System.out.print("이겼습니다!!!");
					user_win += 1;
				}
				System.out.println();
			}
			if(user.equals("보")) {
				if(com == 1) {
					System.out.print("이겼습니다!!!");
					user_win += 1;
				}
				if(com == 2) {
					System.out.print("비겼습니다!!!");
				}
				if(com == 3) {
					System.out.print("졌습니다!!!");
					com_win += 1;
				}
				System.out.println();
			}
			// 이겨야 하는 횟수 도달 or 전체 게임 횟수 도달 전까지 실행
		} while (user_win != win_num && com_win != win_num && now_game_cnt != game_cnt);
		
		// 유저가 승점에 먼저 도달
		if (user_win == win_num)
			System.out.println("### 유저 승!!!");
		// 컴퓨터가 승점에 먼저 도달
		else if (com_win == win_num)
			System.out.println("### 컴퓨터 승!!!");
		// 전체 게임 횟수 도달
		else if (now_game_cnt ==  game_cnt) {
			// 컴퓨터가 이긴 횟수 > 유저가 이긴 횟수
			if (com_win > user_win)
				System.out.println("### 컴퓨터 승!!!");
			// 유저가 이긴 횟수 > 컴퓨터가 이긴 횟수
			else if (user_win > com_win)
				System.out.println("### 유저 승!!!");
			// 컴퓨터가 이긴 횟수 == 유저가 이긴 횟수
			else
				System.out.println("### 비겼습니다!!!");
		}
	}
}
