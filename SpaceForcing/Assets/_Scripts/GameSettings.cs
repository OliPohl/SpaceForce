using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "GameSettings", menuName = "CustomSettings/GameSettings", order = 0)]

public class GameSettings : ScriptableObject
{
    [Header("Background Settings")]
    [Range(0.0f, 10f)] [SerializeField] public float SkySpeed = 0.01f;
    [Range(0.0f, 10f)] [SerializeField] public float WaterSpeed = 0.015f;
}
