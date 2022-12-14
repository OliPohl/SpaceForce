using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "GameSettings", menuName = "CustomSettings/GameSettings", order = 0)]

public class GameSettings : ScriptableObject
{
    [Header("Background Settings")]
    [Range(0.0f, 10.0f)] [SerializeField] public float SkySpeed = 2.0f;
    [Range(0.0f, 10.0f)] [SerializeField] public float WaterSpeed = 3.0f;


    [Header("Spaceship Settings")]
    [Range(0.0f, 10.0f)] [SerializeField] public float SpaceshipSpeed = 5.0f;
    [Range(0.0f, 10.0f)] [SerializeField] public float ProjectileSpeed = 7.0f;
    [Range(0.0f, 10.0f)] [SerializeField] public float ReloadSpeed = 3.0f;
    [Range(1, 10)] [SerializeField] public float MaxHealth = 3;
    [Range(0.0f, 10.0f)] [SerializeField] public float InvulnerableTime = 3.0f;


    [Header("Cube Settings")]
    [Range(0.0f, 10.0f)] [SerializeField] public float CubeSpawnrate = 5.0f;
    [Range(0.0f, 10.0f)] [SerializeField] public float CubeSpeed = 5.0f;
    [Range(0.0f, 10.0f)] [SerializeField] public float BobbingHeight = 5.0f;
    [Range(0, 10)] [SerializeField] public int CubeMaxHealth = 5;


    [Header("Wall Settings")]
    [Range(0.0f, 10.0f)] [SerializeField] public float WallSpeed = 5.0f;
    [Range(0, 10)] [SerializeField] public int GateMaxHealth = 3;
}
