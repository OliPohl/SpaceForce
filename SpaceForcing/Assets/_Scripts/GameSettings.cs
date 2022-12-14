using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "GameSettings", menuName = "CustomSettings/GameSettings", order = 0)]

public class GameSettings : ScriptableObject
{
    [Header("Background Settings")]
    [Range(0.0f, 10.0f)] [SerializeField] public float SkySpeed = 4.0f;
    [Range(0.0f, 10.0f)] [SerializeField] public float WaterSpeed = 10.0f;
}
